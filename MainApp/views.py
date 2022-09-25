from django.db.models import Q
from django.utils.http import urlsafe_base64_encode
from django.utils.timezone import utc
import os
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.http import JsonResponse
from django.views.generic import ListView, FormView, DetailView, View, TemplateView
from .forms import *
from HostingApp.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from .functions import *

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


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
    if cache.get('Blogsmodel'):
        model = cache.get('Blogsmodel')
    else:
        model = Blogs
        cache.set('Blogsmodel', model)
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
        next, prev = get_blog_object_pagination(self.model, self.object)
        context['prev'] = prev
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
        if name == 'contactus':
            obj = ContactUsModel.objects.all()
            title = 'Contact Us Comments'
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
        if name == 'contactus':
            obj = ContactUsModel

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
            # send Email for verification
            e_verify = EmailVerification.objects.filter(user=user).first()
            if e_verify:
                msg_plain = render_to_string('email/email.txt')
                verify_link = HOST_NAME + '/verify/' + str(e_verify.activation_key)
                msg_html = render_to_string('email/emailverification.html',
                                            context={'username': user.username, 'email': user.email,
                                                     'verify_link': verify_link, 'host_name': settings.HOST_NAME})
                send_mail("For the w3code.tech account verification", msg_plain, settings.EMAIL_HOST_USER,
                          [user.email], html_message=msg_html, fail_silently=True)
                # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, f"Verify code has been send your email {user.email}")
            return HttpResponseRedirect(reverse_lazy('w3c:index'))

        errors_str = "Unsuccessful registration. Invalid information/Your Account maybe not activate first activate.>>>>"
        for error in form.errors:
            errors_str += ' '.join(form.errors.get(error)) + '>>>>'
        messages.error(request, errors_str)
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
        user = User.objects.get(username=request.user)
        context = {
            'title': str(request.user).title() + "' Dashboard",
            'type': 'dashboard',
            'user': user,
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
        p_form = ProfileUpdateForm(instance=request.user.profileimage)
        context = {
            'title': 'Profile Update',
            'type': 'update',
            'form': form,
            'p_form': p_form
        }
        return render(request, 'w3c/profile.html', context)

    def post(self, request, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profileimage)
        context = {
            'title': 'Profile Update',
            'type': 'update',
            'form': form,
            'p_form': p_form
        }
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
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
        file_date = datetime.datetime.now().strftime("%Y_%m_%d-%I-%M-%S_%p")
        file_path = os.path.join(path, file_date + file_obj.name)
        file_url = f"{settings.MEDIA_URL}tinymce/{file_date + file_obj.name}"
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


class VerifyAccount(View):
    def get(self, request, key):
        # First check all the expired key if any delete and delete the user whose is not verify
        try:
            for obj in EmailVerification.objects.all():
                now = datetime.datetime.utcnow().replace(tzinfo=utc)
                diff = now - obj.key_expires
                if diff.days > 2:
                    obj.delete()
            for obj in User.objects.all():
                now = datetime.datetime.utcnow().replace(tzinfo=utc)
                diff = now - obj.date_joined
                if diff.days > 2 and obj.is_active == False:
                    obj.delete()
        except Exception as e:
            print("Exception", e)

        obj = EmailVerification.objects.filter(activation_key=key).first()
        if obj:
            user = User.objects.filter(username=obj.user).first()
            user.is_active = True
            user.save()
            messages.success(request,
                             f'Your account has been verified Now you can login UserName:{user} Email:{user.email}')

        else:
            messages.error(request, 'Your activation key has been expired please registration again !')
        return HttpResponseRedirect(reverse_lazy('w3c:index'))


# Contact Us
class ContactUsView(TemplateView, FormView):
    form_class = ContactUsCommentForm
    template_name = 'about/contactus.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_mail(f"{request.POST.get('name')} is Contact to you {request.POST.get('email')}",
                          request.POST.get('body'),
                          settings.EMAIL_HOST_USER, ["maliksakib347@gmail.com"], fail_silently=True)
            except:
                pass
            messages.success(request,
                             'Your Query has been successfully send, Soon i will responses you on your email address')
        else:
            messages.error(request, "Your Query has any error please right details")
            return render(request, self.template_name, {'form': form})

        return HttpResponseRedirect(reverse_lazy('w3c:index'))


class AboutUsView(TemplateView):
    template_name = 'about/aboutus.html'


class PasswordResetRequest(TemplateView, FormView):
    template_name = 'password/password_reset.html'
    form_class = PasswordResetForm

    def form_valid(self, form):
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Request"
                    email_template_plain = 'password/password_reset_email.txt'
                    email_template_html = 'password/mailpasswordreset.html'
                    c = {
                        'email': user.email,
                        'host_name': settings.HOST_NAME,
                        'site_name': 'w3code.tech',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user)
                    }
                    email_plain = render_to_string(email_template_plain, c)
                    email_html = render_to_string(email_template_html, c)
                    try:
                        send_mail(subject, email_plain, settings.EMAIL_HOST_USER, [user.email], html_message=email_html,
                                  fail_silently=True)
                    except BadHeaderError:
                        return HttpResponse('Invalid Header found')
                return HttpResponseRedirect(reverse_lazy('password_reset_done'))
            else:
                messages.error(self.request, "You email is Incorrect")
                return HttpResponseRedirect(reverse_lazy('w3c:index'))
            return super(PasswordResetRequest, self).form_valid(form)


# Privacy Policy

class PrivacyPolicyView(TemplateView):
    template_name = 'w3c/privacypolicy.html'


# Author
class AuthorView(View):
    def get(self, request, name):
        username = name
        user = User.objects.filter(username=username).first()
        context = {
            'user': user
        }
        return render(request, 'w3c/author.html', context)
