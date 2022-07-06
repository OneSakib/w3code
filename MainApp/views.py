import os
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.http import JsonResponse
from django.views.generic import ListView, FormView, DetailView, View
from .models import *
from .forms import *
from next_prev import next_in_order, prev_in_order
from MsApp.models import *
from HostingApp.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'host_name': settings.HOST_NAME
        }
        return render(request, 'w3c/index.html', context)


def OnlineCompiler(request, slug):
    code = None
    slug = str(slug).strip()
    if slug.lower() == 'python':
        code = 'https://trinket.io/embed/python3/70715ff3af'
    elif slug.lower() == 'java':
        code = 'https://trinket.io/embed/java/ebdae30f29'
    elif slug.lower() == 'r':
        code = 'https://trinket.io/embed/R/b0a483cf9b'
    elif slug.lower() == 'html':
        code = 'https://trinket.io/embed/html/592c0c15e7'
    context = {
        'code': code
    }
    return render(request, 'w3c/onlineide.html', context)


class BlogView(ListView):
    template_name = 'w3c/blog.html'
    model = Blogs


class BlogDetailView(DetailView, FormView):
    template_name = 'w3c/blogdetail.html'
    form_class = BlogCommentForm
    model = Blogs
    like_obj = BlogsLike

    def get_ip_address(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comments'] = BlogComments.objects.filter(post=self.object)
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        currentpost = self.object
        prev = prev_in_order(currentpost)
        next = next_in_order(currentpost)
        context['prev'] = None
        context['next'] = None
        if prev != None:
            context['prev'] = prev
        if next != None:
            context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            post_obj = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.instance.post = post_obj
            if form.is_valid():
                ip_address = self.get_ip_address()
                post_len = len(BlogComments.objects.filter(post=post_obj, ip_address=ip_address))
                if post_len < 3:
                    form.instance.ip_address = ip_address
                    form.save()
                    messages.success(request, 'Comment Success')
                else:
                    messages.error(request, "Your comment Range is Full. You can't comment")

            return HttpResponseRedirect(reverse_lazy('w3c:blogdetail', kwargs={'slug': self.kwargs['slug']}))
        else:

            pk = request.POST.get('pk')
            user = User.objects.get(username=request.user)
            context = {}
            if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
                o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
                o.delete()
                context['ok'] = 'delete'
            else:
                self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
                context['ok'] = 'create'
            context['number'] = self.like_obj.objects.all().count()
            return JsonResponse(context)


@method_decorator(login_required(login_url=reverse_lazy('w3c:register')), name='dispatch')
class CommentsView(View):
    def get(self, request):
        return render(request, 'comments/list.html')


@method_decorator(login_required(login_url='/'), name='dispatch')
class CommentsDetailView(View):
    def get(self, request, slug):
        name = str(slug).strip()
        obj = None
        title = 'Comments'
        if name == 'blog':
            obj = BlogComments.objects.all()
            title = 'Blogs Comments'
        if obj != None:
            obj = obj[:50:-1]
        context = {
            'obj': obj,
            'title': title
        }
        return render(request, 'comments/detail.html', context)

    def post(self, request, slug):
        pk = request.POST.get('id')
        name = str(slug).strip()
        if name == 'blog':
            obj = BlogComments

        if obj != None:
            obj = obj.objects.get(pk=pk)
            obj.delete()
        return HttpResponseRedirect(reverse_lazy('w3c:commentsdetail', kwargs={'slug': slug}))


class RegisterUser(View):
    def post(self, request, **kwargs):
        current_url = request.POST.get('currenturl')
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return HttpResponseRedirect(reverse_lazy('w3c:index'))
        errors_str = "Unsuccessful registration. Invalid information.>>>>"
        for error in form.errors:
            errors_str += ' '.join(form.errors.get(error)) + '>>>>'
        messages.error(request, errors_str)
        print(request.path)
        return HttpResponseRedirect(current_url)


class LoginUser(View):
    def post(self, request, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as  {username} .")
                return HttpResponseRedirect(reverse_lazy('w3c:index'))
            else:
                messages.error(request, "Invalid username or password.")
        messages.error(request, "Invalid username or password.")
        return HttpResponseRedirect(reverse_lazy('w3c:index'))


@method_decorator(login_required(login_url=reverse_lazy('w3c:index')), name='dispatch')
class UserLogout(View):
    def get(self, request, **kwargs):
        logout(request)
        messages.info(request, "You have successfully logout")
        return HttpResponseRedirect(reverse_lazy('w3c:index'))


@method_decorator(login_required(login_url=reverse_lazy('w3c:index')), name='dispatch')
class UserProfile(View):
    def get(self, request, **kwargs):
        context = {
            'title': str(request.user).title() + "' Dashboard",
            'type': 'dashboard',
            'user': User.objects.get(username=request.user)
        }
        return render(request, 'w3c/profile.html', context)


@method_decorator(login_required(login_url=reverse_lazy('w3c:index')), name='dispatch')
class UserSaveArticle(View):
    def get(self, request, **kwargs):
        user = User.objects.get(username=request.user)
        data = ArticleBookmark.objects.filter(user=user)
        context = {
            'title': 'Saved Article',
            'type': 'article',
            'data': data
        }
        return render(request, 'w3c/profile.html', context)


@method_decorator(login_required(login_url=reverse_lazy('w3c:index')), name='dispatch')
class UserProfileUpdate(View):
    def get(self, request, **kwargs):
        form = UserUpdateForm(instance=request.user)
        context = {
            'title': 'Profile Update',
            'type': 'update',
            'form': form
        }
        return render(request, 'w3c/profile.html', context)

    def post(self, request, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)
        context = {
            'title': 'Profile Update',
            'type': 'update',
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been updated')
            return HttpResponseRedirect(reverse_lazy('w3c:profile'))
        return render(request, 'w3c/profile.html', context)


class Bookmark(View):
    def post(self, request, **kwargs):
        title = request.POST.get('title')
        link = request.POST.get('url')
        user = User.objects.get(username=request.user)
        data = {}
        obj = ArticleBookmark.objects.filter(user=user, link=link)
        print(request.user.articlebookmark.filter(link=link))
        if obj.exists():
            obj = obj.first()
            obj.delete()
            data['ok'] = 'delete'
        else:
            ArticleBookmark.objects.create(user=user, title=title, link=link)
            data['ok'] = 'create'
        return JsonResponse({'data': data})


# Error page

def error_404(request, exception):
    data = {}
    return render(request, 'error.html', status=404)


# Image for the post Upload
@method_decorator(csrf_exempt, name='dispatch')
class ImageUpload(View):
    def post(self, request, **kwargs):
        file_obj = request.FILES['file']
        file_name_suffix = file_obj.name.split('.')[-1]
        if file_name_suffix not in ["jpg", "png"]:
            return JsonResponse({"message": "Wrong File Format"})
        path = os.path.join(settings.MEDIA_ROOT, 'tinymce', )
        # if there is not such path create it
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.join(path, file_obj.name)
        file_url = f"{settings.MEDIA_URL}tinymce/{file_obj.name}"
        if os.path.exists(file_path):
            return JsonResponse({
                "message": "File already exist",
                "location": file_url
            })
        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        return JsonResponse({
            "message": "Image Uploaded Successfully",
            "location": file_url
        })
