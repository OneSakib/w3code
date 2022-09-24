from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *


# Create your views here.

class HtmlView(View):
    def get(self, request):
        slug = HTMLs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:htmldetail', kwargs={'slug': slug}))


class HTMLDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('HTMLsmodel') and cache.get('HTMLsparent_obj'):
        model = cache.get('HTMLsmodel')
        parent_obj = cache.get('HTMLsparent_obj')
    else:
        model = HTMLs
        parent_obj = HTMLsParent
        cache.set('HTMLsmodel', model)
        cache.set('HTMLsparent_obj', parent_obj)
    like_obj = HTMLsLike

    def get_context_data(self, **kwargs):
        context = super(HTMLDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'HTML'
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


class CSSView(View):
    def get(self, request):
        slug = CSSs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:cssdetail', kwargs={'slug': slug}))


class CSSDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('CSSsmodel') and cache.get('CSSsparent_obj'):
        model = cache.get('CSSsmodel')
        parent_obj = cache.get('CSSsparent_obj')
    else:
        model = CSSs
        parent_obj = CSSsParent
        cache.set('CSSsmodel', model)
        cache.set('CSSsparent_obj', parent_obj)
    like_obj = CSSsLike

    def get_context_data(self, **kwargs):
        context = super(CSSDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'CSS'
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


class LaravelView(View):
    def get(self, request):
        slug = Laravels.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:laraveldetail', kwargs={'slug': slug}))


class LaravelDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Laravelsmodel') and cache.get('Laravelsparent_obj'):
        model = cache.get('Laravelsmodel')
        parent_obj = cache.get('Laravelsparent_obj')
    else:
        model = Laravels
        parent_obj = LaravelsParent
        cache.set('Laravelsmodel', model)
        cache.set('Laravelsparent_obj', parent_obj)
    like_obj = LaravelsLike

    def get_context_data(self, **kwargs):
        context = super(LaravelDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Laravel'
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


class WordpressView(View):
    def get(self, request):
        slug = Wordpress.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:wordpressdetail', kwargs={'slug': slug}))


class WordpressDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Wordpressmodel') and cache.get('Wordpressparent_obj'):
        model = cache.get('Wordpressmodel')
        parent_obj = cache.get('Wordpressparent_obj')
    else:
        model = Wordpress
        parent_obj = WordpressParent
        cache.set('Wordpressmodel', model)
        cache.set('Wordpressparent_obj', parent_obj)
    like_obj = WordpressLike

    def get_context_data(self, **kwargs):
        context = super(WordpressDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Wordpress'
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


class JSONView(View):
    def get(self, request):
        slug = JSONs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:jsondetail', kwargs={'slug': slug}))


class JSONDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('JSONsmodel') and cache.get('JSONsparent_obj'):
        model = cache.get('JSONsmodel')
        parent_obj = cache.get('JSONsparent_obj')
    else:
        model = JSONs
        parent_obj = JSONsParent
        cache.set('JSONsmodel', model)
        cache.set('JSONsparent_obj', parent_obj)
    like_obj = JSONsLike

    def get_context_data(self, **kwargs):
        context = super(JSONDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'JSON'
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


class AJAXView(View):
    def get(self, request):
        slug = Ajaxs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:ajaxdetail', kwargs={'slug': slug}))


class AJAXDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Ajaxsmodel') and cache.get('Ajaxsparent_obj'):
        model = cache.get('Ajaxsmodel')
        parent_obj = cache.get('Ajaxsparent_obj')
    else:
        model = Ajaxs
        parent_obj = AjaxsParent
        cache.set('Ajaxsmodel', model)
        cache.set('Ajaxsparent_obj', parent_obj)
    like_obj = AjaxsLike

    def get_context_data(self, **kwargs):
        context = super(AJAXDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'AJAX'
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


class BootstrapView(View):
    def get(self, request):
        slug = Bootstraps.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:bootstrapdetail', kwargs={'slug': slug}))


class BootstrapDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Bootstrapsmodel') and cache.get('Bootstrapsparent_obj'):
        model = cache.get('Bootstrapsmodel')
        parent_obj = cache.get('Bootstrapsparent_obj')
    else:
        model = Bootstraps
        parent_obj = BootstrapsParent
        cache.set('Bootstrapsmodel', model)
        cache.set('Bootstrapsparent_obj', parent_obj)
    like_obj = BootstrapsLike

    def get_context_data(self, **kwargs):
        context = super(BootstrapDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Bootstrap'
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
