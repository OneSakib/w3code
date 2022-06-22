from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, FormView, DetailView
from .models import *
from .forms import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy


# Create your views here.

class DockerView(View):
    def get(self, request):
        slug = Docker.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:dockerdetail', kwargs={'slug': slug}))


class DockerDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = DockerCommentsForm
    model = Docker

    def get_context_data(self, **kwargs):
        context = super(DockerDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DockerComments.objects.filter(post=self.object)
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
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('VC:dockerdetail', kwargs={'slug': self.kwargs['slug']}))


class GitView(View):
    def get(self, request):
        slug = Gits.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:gitdetail', kwargs={'slug': slug}))


class GitDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = GitsCommentsForm
    model = Gits

    def get_context_data(self, **kwargs):
        context = super(GitDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = GitsComments.objects.filter(post=self.object)
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
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('VC:gitdetail', kwargs={'slug': self.kwargs['slug']}))


class GithubView(View):
    def get(self, request):
        slug = Githubs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:githubdetail', kwargs={'slug': slug}))


class GitHubDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = GithubsCommentsForm
    model = Githubs

    def get_context_data(self, **kwargs):
        context = super(GitHubDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = GithubsComments.objects.filter(post=self.object)
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
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('VC:githubdetail', kwargs={'slug': self.kwargs['slug']}))
