from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import prev_in_order, next_in_order
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *


# Create your views here.
class MSExcelView(View):
    def get(self, request):
        slug = MSExcel.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('MS:msexceldetail', kwargs={'slug': slug}))


class MSExcelDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('MSExcelmodel') and cache.get('MSExcelparent_obj'):
        model = cache.get('MSExcelmodel')
        parent_obj = cache.get('MSExcelparent_obj')
    else:
        model = MSExcel
        parent_obj = MSExcelParent
        cache.set('MSExcelmodel', model)
        cache.set('MSExcelparent_obj', parent_obj)
    like_obj = MSExcelLike

    def get_context_data(self, **kwargs):
        context = super(MSExcelDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'MS Excel'
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


class MSWordView(View):
    def get(self, request):
        slug = MSWord.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('MS:msworddetail', kwargs={'slug': slug}))


class MSWordDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('MSWordmodel') and cache.get('MSWordparent_obj'):
        model = cache.get('MSWordmodel')
        parent_obj = cache.get('MSWordparent_obj')
    else:
        model = MSWord
        parent_obj = MSWordParent
        cache.set('MSWordmodel', model)
        cache.set('MSWordparent_obj', parent_obj)
    like_obj = MSWordLike

    def get_context_data(self, **kwargs):
        context = super(MSWordDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'MS Word'
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


class MSPowerpointView(View):
    def get(self, request):
        slug = MSPowerpoint.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('MS:mspowerpointdetail', kwargs={'slug': slug}))


class MSPowerpointDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('MSPowerpointmodel') and cache.get('MSPowerpointparent_obj'):
        model = cache.get('MSPowerpointmodel')
        parent_obj = cache.get('MSPowerpointparent_obj')
    else:
        model = MSPowerpoint
        parent_obj = MSPowerpointParent
        cache.set('MSPowerpointmodel', model)
        cache.set('MSPowerpointparent_obj', parent_obj)
    like_obj = MSPowerpointLike

    def get_context_data(self, **kwargs):
        context = super(MSPowerpointDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'MS Powerpoint'
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


class MSOneNoteView(View):
    def get(self, request):
        slug = MSOneNote.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('MS:msonenotedetail', kwargs={'slug': slug}))


class MSOneNoteDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('MSOneNotemodel') and cache.get('MSOneNoteparent_obj'):
        model = cache.get('MSOneNotemodel')
        parent_obj = cache.get('MSOneNoteparent_obj')
    else:
        model = MSOneNote
        parent_obj = MSOneNoteParent
        cache.set('MSOneNotemodel', model)
        cache.set('MSOneNoteparent_obj', parent_obj)
    like_obj = MSOneNoteLike

    def get_context_data(self, **kwargs):
        context = super(MSOneNoteDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'MS One Note'
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
