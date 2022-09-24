from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import View, DetailView
from .models import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *


# Create your views here.
class CView(View):
    def get(self, request):
        slug = CLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:cdetail', kwargs={'slug': slug}))


class CLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('CLanguagemodel') and cache.get('CLanguageparent_obj'):
        model = cache.get('CLanguagemodel')
        parent_obj = cache.get('CLanguageparent_obj')
    else:
        model = CLanguage
        parent_obj = CLanguageParent
        cache.set('CLanguagemodel', model)
        cache.set('CLanguageparent_obj', parent_obj)
    like_obj = CLanguageLike

    def get_context_data(self, **kwargs):
        context = super(CLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C Language'
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


class CPlusView(View):
    def get(self, request):
        slug = CplusLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:cplusdetail', kwargs={'slug': slug}))


class CPlusLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('CplusLanguagemodel') and cache.get('CplusLanguageparent_obj'):
        model = cache.get('CplusLanguagemodel')
        parent_obj = cache.get('CplusLanguageparent_obj')
    else:
        model = CplusLanguage
        parent_obj = CLanguageParent
        cache.set('CplusLanguagemodel', model)
        cache.set('CplusLanguageparent_obj', parent_obj)
    like_obj = CplusLanguageLike

    def get_context_data(self, **kwargs):
        context = super(CPlusLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C++ Language'
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


class PythonView(View):
    def get(self, request):
        slug = PythonLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:pythondetail', kwargs={'slug': slug}))


class PythonLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('PythonLanguagemodel') and cache.get('PythonLanguageparent_obj'):
        model = cache.get('PythonLanguagemodel')
        parent_obj = cache.get('PythonLanguageparent_obj')
    else:
        model = PythonLanguage
        parent_obj = PythonLanguageParent
        cache.set('PythonLanguagemodel', model)
        cache.set('PythonLanguageparent_obj', parent_obj)
    like_obj = PythonLanguageLike

    def get_context_data(self, **kwargs):
        context = super(PythonLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Python Language'
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


class JavaView(View):
    def get(self, request):
        slug = JavaLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:javadetail', kwargs={'slug': slug}))


class JavaLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('JavaLanguagemodel') and cache.get('JavaLanguageparent_obj'):
        model = cache.get('JavaLanguagemodel')
        parent_obj = cache.get('JavaLanguageparent_obj')
    else:
        model = JavaLanguage
        parent_obj = JavaLanguageParent
        cache.set('JavaLanguagemodel', model)
        cache.set('JavaLanguageparent_obj', parent_obj)
    like_obj = JavaLanguageLike

    def get_context_data(self, **kwargs):
        context = super(JavaLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Java Language'
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


class AndroidView(View):
    def get(self, request):
        slug = AndroidLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:androiddetail', kwargs={'slug': slug}))


class AndroidLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('AndroidLanguagemodel') and cache.get('AndroidLanguageparent_obj'):
        model = cache.get('AndroidLanguagemodel')
        parent_obj = cache.get('AndroidLanguageparent_obj')
    else:
        model = AndroidLanguage
        parent_obj = AndroidLanguageParent
        cache.set('AndroidLanguagemodel', model)
        cache.set('AndroidLanguageparent_obj', parent_obj)
    like_obj = AndroidLanguageLike

    def get_context_data(self, **kwargs):
        context = super(AndroidLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Android'
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


class KotlinView(View):
    def get(self, request):
        slug = KotlinLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:kotlindetail', kwargs={'slug': slug}))


class KotlinLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('KotlinLanguagemodel') and cache.get('KotlinLanguageparent_obj'):
        model = cache.get('KotlinLanguagemodel')
        parent_obj = cache.get('KotlinLanguageparent_obj')
    else:
        model = KotlinLanguage
        parent_obj = KotlinLanguageParent
        cache.set('KotlinLanguagemodel', model)
        cache.set('KotlinLanguageparent_obj', parent_obj)
    like_obj = KotlinLanguageLike

    def get_context_data(self, **kwargs):
        context = super(KotlinLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Kotlin'
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


class RView(View):
    def get(self, request):
        slug = RLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:rdetail', kwargs={'slug': slug}))


class RLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('RLanguagemodel') and cache.get('RLanguageparent_obj'):
        model = cache.get('RLanguagemodel')
        parent_obj = cache.get('RLanguageparent_obj')
    else:
        model = RLanguage
        parent_obj = RLanguageParent
        cache.set('RLanguagemodel', model)
        cache.set('RLanguageparent_obj', parent_obj)
    like_obj = RLanguageLike

    def get_context_data(self, **kwargs):
        context = super(RLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'R Language'
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


class CSharpView(View):
    def get(self, request):
        slug = CsharpLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:csharpdetail', kwargs={'slug': slug}))


class CSharpLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('CsharpLanguagemodel') and cache.get('CsharpLanguageparent_obj'):
        model = cache.get('CsharpLanguagemodel')
        parent_obj = cache.get('CsharpLanguageparent_obj')
    else:
        model = CsharpLanguage
        parent_obj = CsharpLanguageParent
        cache.set('CsharpLanguagemodel', model)
        cache.set('CsharpLanguageparent_obj', parent_obj)
    like_obj = CsharpLanguageLike

    def get_context_data(self, **kwargs):
        context = super(CSharpLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C# Language'
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


class SwiftView(View):
    def get(self, request):
        slug = SwiftLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:swiftdetail', kwargs={'slug': slug}))


class SwiftLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('SwiftLanguagemodel') and cache.get('SwiftLanguageparent_obj'):
        model = cache.get('SwiftLanguagemodel')
        parent_obj = cache.get('SwiftLanguageparent_obj')
    else:
        model = SwiftLanguage
        parent_obj = SwiftLanguageParent
        cache.set('SwiftLanguagemodel', model)
        cache.set('SwiftLanguageparent_obj', parent_obj)
    like_obj = SwiftLanguageLike

    def get_context_data(self, **kwargs):
        context = super(SwiftLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Swift Language'
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


class JavaScriptView(View):
    def get(self, request):
        slug = JavaScriptLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:javascriptdetail', kwargs={'slug': slug}))


class JavaScriptLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('JavaScriptLanguagemodel') and cache.get('JavaScriptLanguageparent_obj'):
        model = cache.get('JavaScriptLanguagemodel')
        parent_obj = cache.get('JavaScriptLanguageparent_obj')
    else:
        model = JavaScriptLanguage
        parent_obj = JavaScriptLanguageParent
        cache.set('JavaScriptLanguagemodel', model)
        cache.set('JavaScriptLanguageparent_obj', parent_obj)
    like_obj = JavaScriptLanguageLike

    def get_context_data(self, **kwargs):
        context = super(JavaScriptLanguageDetailView, self).get_context_data(**kwargs)
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

        context['title'] = 'JavaScript'
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


class PHPView(View):
    def get(self, request):
        slug = PHPLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:phpdetail', kwargs={'slug': slug}))


class PHPLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('PHPLanguagemodel') and cache.get('PHPLanguageparent_obj'):
        model = cache.get('PHPLanguagemodel')
        parent_obj = cache.get('PHPLanguageparent_obj')
    else:
        model = PHPLanguage
        parent_obj = PHPLanguageParent
        cache.set('PHPLanguagemodel', model)
        cache.set('PHPLanguageparent_obj', parent_obj)
    like_obj = PHPLanguageLike

    def get_context_data(self, **kwargs):
        context = super(PHPLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'PHP Language'
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


class DotNetView(View):
    def get(self, request):
        slug = DotNetLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:dotnetdetail', kwargs={'slug': slug}))


class DotNetLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    if cache.get('DotNetLanguagemodel') and cache.get('DotNetLanguageparent_obj'):
        model = cache.get('DotNetLanguagemodel')
        parent_obj = cache.get('DotNetLanguageparent_obj')
    else:
        model = DotNetLanguage
        parent_obj = DotNetLanguageParent
        cache.set('DotNetLanguagemodel', model)
        cache.set('DotNetLanguageparent_obj', parent_obj)
    like_obj = DotNetLanguageLike

    def get_context_data(self, **kwargs):
        context = super(DotNetLanguageDetailView, self).get_context_data(**kwargs)
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
        context['title'] = '.NET Language'
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
