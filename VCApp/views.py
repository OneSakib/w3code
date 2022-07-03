from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy


# Create your views here.

class DockerView(View):
    def get(self, request):
        slug = Docker.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:dockerdetail', kwargs={'slug': slug}))


class DockerDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Docker

    def get_context_data(self, **kwargs):
        context = super(DockerDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Docker'
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



class GitView(View):
    def get(self, request):
        slug = Gits.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:gitdetail', kwargs={'slug': slug}))


class GitDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Gits

    def get_context_data(self, **kwargs):
        context = super(GitDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'GIT'
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



class GithubView(View):
    def get(self, request):
        slug = Githubs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:githubdetail', kwargs={'slug': slug}))


class GitHubDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Githubs

    def get_context_data(self, **kwargs):
        context = super(GitHubDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'GitHub'
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

