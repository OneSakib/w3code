from django.shortcuts import HttpResponseRedirect
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy
from django.views.generic import View, DetailView
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *


# Create your views here.
class CProgrammeView(View):
    def get(self, request):
        slug = CProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:cprogrammedetail', kwargs={'slug': slug}))


class CProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('CProgrammemodel') and cache.get('CProgrammeparent_obj'):
        model = cache.get('CProgrammemodel')
        parent_obj = cache.get('CProgrammeparent_obj')
    else:
        model = CProgramme
        parent_obj = CProgrammeParent
        cache.set('CProgrammemodel', model)
        cache.set('CProgrammeparent_obj', parent_obj)
    like_obj = CProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(CProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C Programme'
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


class CPlusProgrammeView(View):
    def get(self, request):
        slug = CPlusProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:cplusprogrammedetail', kwargs={'slug': slug}))


class CPlusProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('CPlusProgrammemodel') and cache.get('CPlusProgrammeparent_obj'):
        model = cache.get('CPlusProgrammemodel')
        parent_obj = cache.get('CPlusProgrammeparent_obj')
    else:
        model = CPlusProgramme
        parent_obj = CPlusProgrammeParent
        cache.set('CPlusProgrammemodel', model)
        cache.set('CPlusProgrammeparent_obj', parent_obj)
    like_obj = CPlusProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(CPlusProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C++ Programme'
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


class PythonProgrammeView(View):
    def get(self, request):
        slug = PythonProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:pythonprogrammedetail', kwargs={'slug': slug}))


class PythonProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('PythonProgrammemodel') and cache.get('PythonProgrammeparent_obj'):
        model = cache.get('PythonProgrammemodel')
        parent_obj = cache.get('PythonProgrammeparent_obj')
    else:
        model = PythonProgramme
        parent_obj = PythonProgrammeParent
        cache.set('PythonProgrammemodel', model)
        cache.set('PythonProgrammeparent_obj', parent_obj)
    like_obj = PythonProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(PythonProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Python Programme'
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


class JavaProgrammeView(View):
    def get(self, request):
        slug = JavaProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:javaprogrammedetail', kwargs={'slug': slug}))


class JavaProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('JavaProgrammemodel') and cache.get('JavaProgrammeparent_obj'):
        model = cache.get('JavaProgrammemodel')
        parent_obj = cache.get('JavaProgrammeparent_obj')
    else:
        model = JavaProgramme
        parent_obj = JavaProgrammeParent
        cache.set('JavaProgrammemodel', model)
        cache.set('JavaProgrammeparent_obj', parent_obj)
    like_obj = JavaProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(JavaProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Java Programme'
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


class KotlinProgrammeView(View):
    def get(self, request):
        slug = KotlinProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:kotlinprogrammedetail', kwargs={'slug': slug}))


class KotlinProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('KotlinProgrammemodel') and cache.get('KotlinProgrammeparent_obj'):
        model = cache.get('KotlinProgrammemodel')
        parent_obj = cache.get('KotlinProgrammeparent_obj')
    else:
        model = KotlinProgramme
        parent_obj = KotlinProgrammeParent
        cache.set('KotlinProgrammemodel', model)
        cache.set('KotlinProgrammeparent_obj', parent_obj)
    like_obj = KotlinProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(KotlinProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Kotlin Programme'
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


class RProgrammeView(View):
    def get(self, request):
        slug = RProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:rprogrammedetail', kwargs={'slug': slug}))


class RProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('RProgrammemodel') and cache.get('RProgrammeparent_obj'):
        model = cache.get('RProgrammemodel')
        parent_obj = cache.get('RProgrammeparent_obj')
    else:
        model = RProgramme
        parent_obj = RProgrammeParent
        cache.set('RProgrammemodel', model)
        cache.set('RProgrammeparent_obj', parent_obj)
    like_obj = RProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(RProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'R Programme'
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


class CSharpProgrammeView(View):
    def get(self, request):
        slug = CSharpProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:csharpprogrammedetail', kwargs={'slug': slug}))


class CSharpProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('CSharpProgrammemodel') and cache.get('CSharpProgrammeparent_obj'):
        model = cache.get('CSharpProgrammemodel')
        parent_obj = cache.get('CSharpProgrammeparent_obj')
    else:
        model = CSharpProgramme
        parent_obj = CSharpProgrammeParent
        cache.set('CSharpProgrammemodel', model)
        cache.set('CSharpProgrammeparent_obj', parent_obj)
    like_obj = CSharpProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(CSharpProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C# Programme'
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


class SwiftProgrammeView(View):
    def get(self, request):
        slug = SwiftProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:swiftprogrammedetail', kwargs={'slug': slug}))


class SwiftProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('SwiftProgrammemodel') and cache.get('SwiftProgrammeparent_obj'):
        model = cache.get('SwiftProgrammemodel')
        parent_obj = cache.get('SwiftProgrammeparent_obj')
    else:
        model = SwiftProgramme
        parent_obj = SwiftProgrammeParent
        cache.set('SwiftProgrammemodel', model)
        cache.set('SwiftProgrammeparent_obj', parent_obj)
    like_obj = SwiftProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(SwiftProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Swift Programme'
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


class JavaScriptProgrammeView(View):
    def get(self, request):
        slug = JavaScriptProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:javascriptprogrammedetail', kwargs={'slug': slug}))


class JavaScriptProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('JavaScriptProgrammemodel') and cache.get('JavaScriptProgrammeparent_obj'):
        model = cache.get('JavaScriptProgrammemodel')
        parent_obj = cache.get('JavaScriptProgrammeparent_obj')
    else:
        model = JavaScriptProgramme
        parent_obj = JavaScriptProgrammeParent
        cache.set('JavaScriptProgrammemodel', model)
        cache.set('JavaScriptProgrammeparent_obj', parent_obj)
    like_obj = JavaScriptProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(JavaScriptProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'JavaScript Programme'
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


class PHPProgrammeView(View):
    def get(self, request):
        slug = PHPProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:phpprogrammedetail', kwargs={'slug': slug}))


class PHPProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('PHPProgrammemodel') and cache.get('PHPProgrammeparent_obj'):
        model = cache.get('PHPProgrammemodel')
        parent_obj = cache.get('PHPProgrammeparent_obj')
    else:
        model = PHPProgramme
        parent_obj = PHPProgrammeParent
        cache.set('PHPProgrammemodel', model)
        cache.set('PHPProgrammeparent_obj', parent_obj)
    like_obj = PHPProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(PHPProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'PHP Programme'
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


class DotNetProgrammeView(View):
    def get(self, request):
        slug = DotNetProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:dotnetprogrammedetail', kwargs={'slug': slug}))


class DotNetProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    if cache.get('DotNetProgrammemodel') and cache.get('DotNetProgrammeparent_obj'):
        model = cache.get('DotNetProgrammemodel')
        parent_obj = cache.get('DotNetProgrammeparent_obj')
    else:
        model = DotNetProgramme
        parent_obj = DotNetProgrammeParent
        cache.set('DotNetProgrammemodel', model)
        cache.set('DotNetProgrammeparent_obj', parent_obj)
    like_obj = DotNetProgrammeLike

    def get_context_data(self, **kwargs):
        context = super(DotNetProgrammeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = '.NET Programme'
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
