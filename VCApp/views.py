from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *

# Create your views here.

class DockerView(View):
    def get(self, request):
        slug = Docker.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:dockerdetail', kwargs={'slug': slug}))



class DockerDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Dockermodel') and cache.get('Dockerparent_obj'):
        model = cache.get('Dockermodel')
        parent_obj = cache.get('Dockerparent_obj')
    else:
        model = Docker
        parent_obj = DockerParent
        cache.set('Dockermodel', model)
        cache.set('Dockerparent_obj', parent_obj)
    like_obj = DockerLike

    def get_context_data(self, **kwargs):
        context = super(DockerDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Docker'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
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


class GitView(View):
    def get(self, request):
        slug = Gits.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:gitdetail', kwargs={'slug': slug}))


class GitDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Gitsmodel') and cache.get('Gitsparent_obj'):
        model = cache.get('Gitsmodel')
        parent_obj = cache.get('Gitsparent_obj')
    else:
        model = Gits
        parent_obj = GithubsParent
        cache.set('Gitsmodel', model)
        cache.set('Gitsparent_obj', parent_obj)
    like_obj = GitsLike

    def get_context_data(self, **kwargs):
        context = super(GitDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'GIT'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
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


class GithubView(View):
    def get(self, request):
        slug = Githubs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('VC:githubdetail', kwargs={'slug': slug}))



class GitHubDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Githubsmodel') and cache.get('Githubsparent_obj'):
        model = cache.get('Githubsmodel')
        parent_obj = cache.get('Githubsparent_obj')
    else:
        model = Githubs
        parent_obj = GithubsParent
        cache.set('Githubsmodel', model)
        cache.set('Githubsparent_obj', parent_obj)
    like_obj = GithubsLike

    def get_context_data(self, **kwargs):
        context = super(GitHubDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'GitHub'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
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
