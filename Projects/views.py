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
class CProjectsView(View):
    def get(self, request):
        slug = CProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:cprojectsdetail', kwargs={'slug': slug}))


class CProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('CProjectsmodel') and cache.get('CProjectsparent_obj'):
        model = cache.get('CProjectsmodel')
        parent_obj = cache.get('CProjectsparent_obj')
    else:
        model = CProjects
        parent_obj = CProjectsParent
        cache.set('CProjectsmodel', model)
        cache.set('CProjectsparent_obj', parent_obj)
    like_obj = CProjectsLike

    def get_context_data(self, **kwargs):
        context = super(CProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C Projects'
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


class CPlusProjectsView(View):
    def get(self, request):
        slug = CPlusProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:cplusprojectsdetail', kwargs={'slug': slug}))


class CPlusProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('CPlusProjectsmodel') and cache.get('CPlusProjectsparent_obj'):
        model = cache.get('CPlusProjectsmodel')
        parent_obj = cache.get('CPlusProjectsparent_obj')
    else:
        model = CPlusProjects
        parent_obj = CPlusProjectsParent
        cache.set('CPlusProjectsmodel', model)
        cache.set('CPlusProjectsparent_obj', parent_obj)
    like_obj = CPlusProjectsLike

    def get_context_data(self, **kwargs):
        context = super(CPlusProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C++ Projects'
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


class PythonProjectsView(View):
    def get(self, request):
        slug = PythonProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:pythonprojectsdetail', kwargs={'slug': slug}))


class PythonProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('PythonProjectsmodel') and cache.get('PythonProjectsparent_obj'):
        model = cache.get('PythonProjectsmodel')
        parent_obj = cache.get('PythonProjectsparent_obj')
    else:
        model = PythonProjects
        parent_obj = PythonProjectsParent
        cache.set('PythonProjectsmodel', model)
        cache.set('PythonProjectsparent_obj', parent_obj)
    like_obj = PythonProjectsLike

    def get_context_data(self, **kwargs):
        context = super(PythonProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Python Projects'
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


class JavaProjectsView(View):
    def get(self, request):
        slug = JavaProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:javaprojectsdetail', kwargs={'slug': slug}))


class JavaProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('JavaProjectsmodel') and cache.get('JavaProjectsparent_obj'):
        model = cache.get('JavaProjectsmodel')
        parent_obj = cache.get('JavaProjectsparent_obj')
    else:
        model = JavaProjects
        parent_obj = JavaProjectsParent
        cache.set('JavaProjectsmodel', model)
        cache.set('JavaProjectsparent_obj', parent_obj)
    like_obj = JavaProjectsLike

    def get_context_data(self, **kwargs):
        context = super(JavaProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Java Projects'
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


class KotlinProjectsView(View):
    def get(self, request):
        slug = KotlinProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:kotlinprojectsdetail', kwargs={'slug': slug}))


class KotlinProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('KotlinProjectsmodel') and cache.get('KotlinProjectsparent_obj'):
        model = cache.get('KotlinProjectsmodel')
        parent_obj = cache.get('KotlinProjectsparent_obj')
    else:
        model = KotlinProjects
        parent_obj = KotlinProjectsParent
        cache.set('KotlinProjectsmodel', model)
        cache.set('KotlinProjectsparent_obj', parent_obj)
    like_obj = KotlinProjectsLike

    def get_context_data(self, **kwargs):
        context = super(KotlinProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Kotlin Projects'
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


class RProjectsView(View):
    def get(self, request):
        slug = RProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:rprojectsdetail', kwargs={'slug': slug}))


class RProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('RProjectsmodel') and cache.get('RProjectsparent_obj'):
        model = cache.get('RProjectsmodel')
        parent_obj = cache.get('RProjectsparent_obj')
    else:
        model = RProjects
        parent_obj = RProjectsParent
        cache.set('RProjectsmodel', model)
        cache.set('RProjectsparent_obj', parent_obj)
    like_obj = RProjectsLike

    def get_context_data(self, **kwargs):
        context = super(RProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'R Projects'
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


class CSharpProjectsView(View):
    def get(self, request):
        slug = CSharpProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:csharpprojectsdetail', kwargs={'slug': slug}))


class CSharpProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('CSharpProjectsmodel') and cache.get('CSharpProjectsparent_obj'):
        model = cache.get('CSharpProjectsmodel')
        parent_obj = cache.get('CSharpProjectsparent_obj')
    else:
        model = CSharpProjects
        parent_obj = CSharpProjectsParent
        cache.set('CSharpProjectsmodel', model)
        cache.set('CSharpProjectsparent_obj', parent_obj)
    like_obj = CSharpProjectsLike

    def get_context_data(self, **kwargs):
        context = super(CSharpProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C# Projects'
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


class SwiftProjectsView(View):
    def get(self, request):
        slug = SwiftProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:swiftprojectsdetail', kwargs={'slug': slug}))


class SwiftProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('SwiftProjectsmodel') and cache.get('SwiftProjectsparent_obj'):
        model = cache.get('SwiftProjectsmodel')
        parent_obj = cache.get('SwiftProjectsparent_obj')
    else:
        model = SwiftProjects
        parent_obj = SwiftProjectsParent
        cache.set('SwiftProjectsmodel', model)
        cache.set('SwiftProjectsparent_obj', parent_obj)
    like_obj = SwiftProjectsLike

    def get_context_data(self, **kwargs):
        context = super(SwiftProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Swift Projects'
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


class JavaScriptProjectsView(View):
    def get(self, request):
        slug = JavaScriptProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:javascriptprojectsdetail', kwargs={'slug': slug}))


class JavaScriptProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('JavaScriptProjectsmodel') and cache.get('JavaScriptProjectsparent_obj'):
        model = cache.get('JavaScriptProjectsmodel')
        parent_obj = cache.get('JavaScriptProjectsparent_obj')
    else:
        model = JavaScriptProjects
        parent_obj = JavaScriptProjectsParent
        cache.set('JavaScriptProjectsmodel', model)
        cache.set('JavaScriptProjectsparent_obj', parent_obj)
    like_obj = JavaScriptProjectsLike

    def get_context_data(self, **kwargs):
        context = super(JavaScriptProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'JavaScript Projects'
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


class PHPProjectsView(View):
    def get(self, request):
        slug = PHPProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:phpprojectsdetail', kwargs={'slug': slug}))


class PHPProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('PHPProjectsmodel') and cache.get('PHPProjectsparent_obj'):
        model = cache.get('PHPProjectsmodel')
        parent_obj = cache.get('PHPProjectsparent_obj')
    else:
        model = PHPProjects
        parent_obj = PHPProjectsParent
        cache.set('PHPProjectsmodel', model)
        cache.set('PHPProjectsparent_obj', parent_obj)
    like_obj = PHPProjectsLike

    def get_context_data(self, **kwargs):
        context = super(PHPProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'PHP Projects'
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


class AndroidProjectView(View):
    def get(self, request):
        slug = AndroidProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:androidprojectsdetail', kwargs={'slug': slug}))


class AndroidProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('AndroidProjectsmodel') and cache.get('AndroidProjectsparent_obj'):
        model = cache.get('AndroidProjectsmodel')
        parent_obj = cache.get('AndroidProjectsparent_obj')
    else:
        model = AndroidProjects
        parent_obj = AndroidProjectsParent
        cache.set('AndroidProjectsmodel', model)
        cache.set('AndroidProjectsparent_obj', parent_obj)
    like_obj = AndroidProjectsLike

    def get_context_data(self, **kwargs):
        context = super(AndroidProjectDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Android Project'
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


class DotNetProjectsView(View):
    def get(self, request):
        slug = DotNetProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:androidprojectsdetail', kwargs={'slug': slug}))


class DotNetProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    if cache.get('DotNetProjectsmodel') and cache.get('DotNetProjectsparent_obj'):
        model = cache.get('DotNetProjectsmodel')
        parent_obj = cache.get('DotNetProjectsparent_obj')
    else:
        model = DotNetProjects
        parent_obj = DotNetProjectsParent
        cache.set('DotNetProjectsmodel', model)
        cache.set('DotNetProjectsparent_obj', parent_obj)
    like_obj = DotNetProjectsLike

    def get_context_data(self, **kwargs):
        context = super(DotNetProjectsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = '.NET Projects'
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
