from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from django.urls import reverse_lazy
from next_prev import prev_in_order, next_in_order
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *


# Create your views here.
class JqueryView(View):
    def get(self, request):
        slug = Jquery.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:jquerydetail', kwargs={'slug': slug}))


class JqueryDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Jquerymodel') and cache.get('Jqueryparent_obj'):
        model = cache.get('Jquerymodel')
        parent_obj = cache.get('Jqueryparent_obj')
    else:
        model = Jquery
        parent_obj = JqueryParent
        cache.set('Jquerymodel', model)
        cache.set('Jqueryparent_obj', parent_obj)
    like_obj = JqueryLike

    def get_context_data(self, **kwargs):
        context = super(JqueryDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'JQuery'
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


class AngularView(View):
    def get(self, request):
        slug = Angularjs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:angulardetail', kwargs={'slug': slug}))


class AngularDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Angularjsmodel') and cache.get('Angularjsparent_obj'):
        model = cache.get('Angularjsmodel')
        parent_obj = cache.get('Angularjsparent_obj')
    else:
        model = Angularjs
        parent_obj = AngularjsParent
        cache.set('Angularjsmodel', model)
        cache.set('Angularjsparent_obj', parent_obj)
    like_obj = AngularjsLike

    def get_context_data(self, **kwargs):
        context = super(AngularDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'AngularJs'
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


class NodejsView(View):
    def get(self, request):
        slug = Nodejs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:nodejsdetail', kwargs={'slug': slug}))


class NodejsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Nodejsmodel') and cache.get('Nodejsparent_obj'):
        model = cache.get('Nodejsmodel')
        parent_obj = cache.get('Nodejsparent_obj')
    else:
        model = Nodejs
        parent_obj = NodejsParent
        cache.set('Nodejsmodel', model)
        cache.set('Nodejsparent_obj', parent_obj)
    like_obj = NodejsLike

    def get_context_data(self, **kwargs):
        context = super(NodejsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'NodeJs'
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


class ExpressjsView(View):
    def get(self, request):
        slug = Expressjs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:expressjsdetail', kwargs={'slug': slug}))


class ExpressjsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Expressjsmodel') and cache.get('Expressjsparent_obj'):
        model = cache.get('Expressjsmodel')
        parent_obj = cache.get('Expressjsparent_obj')
    else:
        model = Expressjs
        parent_obj = ExpressjsParent
        cache.set('Expressjsmodel', model)
        cache.set('Expressjsparent_obj', parent_obj)
    like_obj = ExpressjsLike

    def get_context_data(self, **kwargs):
        context = super(ExpressjsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'ExpressJs'
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


class ReactjsView(View):
    def get(self, request):
        slug = Reactjs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:reactjsdetail', kwargs={'slug': slug}))


class ReactjsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Reactjsmodel') and cache.get('Reactjsparent_obj'):
        model = cache.get('Reactjsmodel')
        parent_obj = cache.get('Reactjsparent_obj')
    else:
        model = Reactjs
        parent_obj = ReactjsParent
        cache.set('Reactjsmodel', model)
        cache.set('Reactjsparent_obj', parent_obj)
    parent_obj = ReactjsParent

    def get_context_data(self, **kwargs):
        context = super(ReactjsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'ReactJS'
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


class TypescriptView(View):
    def get(self, request):
        slug = TypeScripts.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:typescriptdetail', kwargs={'slug': slug}))


class TypescriptDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('TypeScriptsmodel') and cache.get('TypeScriptsparent_obj'):
        model = cache.get('TypeScriptsmodel')
        parent_obj = cache.get('TypeScriptsparent_obj')
    else:
        model = TypeScripts
        parent_obj = TypeScriptsParent
        cache.set('TypeScriptsmodel', model)
        cache.set('TypeScriptsparent_obj', parent_obj)
    like_obj = TypeScriptsLike

    def get_context_data(self, **kwargs):
        context = super(TypescriptDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'TypeScript'
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


class VuejsView(View):
    def get(self, request):
        slug = VUEjs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:vuejsdetail', kwargs={'slug': slug}))


class VuejsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('VUEjsmodel') and cache.get('VUEjsparent_obj'):
        model = cache.get('VUEjsmodel')
        parent_obj = cache.get('VUEjsparent_obj')
    else:
        model = VUEjs
        parent_obj = VUEjsParent
        cache.set('VUEjsmodel', model)
        cache.set('VUEjsparent_obj', parent_obj)
    like_obj = VUEjsLike

    def get_context_data(self, **kwargs):
        context = super(VuejsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'VUEJS'
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
