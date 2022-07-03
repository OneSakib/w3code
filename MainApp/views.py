from django.shortcuts import render, HttpResponseRedirect
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


@method_decorator(login_required(login_url='/'), name='dispatch')
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
