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
class CExerciseView(View):
    def get(self, request):
        slug = CExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:cexercisedetail', kwargs={'slug': slug}))


class CExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('CExercisemodel') and cache.get('CExerciseparent_obj'):
        model = cache.get('CExercisemodel')
        parent_obj = cache.get('CExerciseparent_obj')
    else:
        model = CExercise
        parent_obj = CExerciseParent
        cache.set('CExercisemodel', model)
        cache.set('CExerciseparent_obj', parent_obj)
    like_obj = CExerciseLike

    def get_context_data(self, **kwargs):
        context = super(CExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C Exercise'
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


class CPlusExerciseView(View):
    def get(self, request):
        slug = CPlusExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:cplusexcisedetail', kwargs={'slug': slug}))


class CPlusExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('CPlusExercisemodel') and cache.get('CPlusExerciseparent_obj'):
        model = cache.get('CPlusExercisemodel')
        parent_obj = cache.get('CPlusExerciseparent_obj')
    else:
        model = CPlusExercise
        parent_obj = CPlusExerciseParent
        cache.set('CPlusExercisemodel', model)
        cache.set('CPlusExerciseparent_obj', parent_obj)
    like_obj = CPlusExerciseLike

    def get_context_data(self, **kwargs):
        context = super(CPlusExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C++ Exercise'
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


class PythonExerciseView(View):
    def get(self, request):
        slug = PythonExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:pythonexercisedetail', kwargs={'slug': slug}))


class PythonExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('PythonExercisemodel') and cache.get('PythonExerciseparent_obj'):
        model = cache.get('PythonExercisemodel')
        parent_obj = cache.get('PythonExerciseparent_obj')
    else:
        model = PythonExercise
        parent_obj = PythonExerciseParent
        cache.set('PythonExercisemodel', model)
        cache.set('PythonExerciseparent_obj', parent_obj)
    like_obj = PythonExerciseLike

    def get_context_data(self, **kwargs):
        context = super(PythonExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Python Exercise'
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


class JavaExerciseView(View):
    def get(self, request):
        slug = JavaExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:javaexercisedetail', kwargs={'slug': slug}))


class JavaExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('JavaExercisemodel') and cache.get('JavaExerciseparent_obj'):
        model = cache.get('JavaExercisemodel')
        parent_obj = cache.get('JavaExerciseparent_obj')
    else:
        model = JavaExercise
        parent_obj = JavaExerciseParent
        cache.set('JavaExercisemodel', model)
        cache.set('JavaExerciseparent_obj', parent_obj)
    like_obj = JavaExerciseLike

    def get_context_data(self, **kwargs):
        context = super(JavaExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Java Exercise'
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


class KotlinExerciseView(View):
    def get(self, request):
        slug = KotlinExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:kotlinexercisedetail', kwargs={'slug': slug}))


class KotlinExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('KotlinExercisemodel') and cache.get('KotlinExerciseparent_obj'):
        model = cache.get('KotlinExercisemodel')
        parent_obj = cache.get('KotlinExerciseparent_obj')
    else:
        model = KotlinExercise
        parent_obj = KotlinExerciseParent
        cache.set('KotlinExercisemodel', model)
        cache.set('KotlinExerciseparent_obj', parent_obj)
    like_obj = KotlinExerciseLike

    def get_context_data(self, **kwargs):
        context = super(KotlinExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Kotlin Exercise'
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


class RExerciseView(View):
    def get(self, request):
        slug = RExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:rexercisedetail', kwargs={'slug': slug}))


class RExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('RExercisemodel') and cache.get('RExerciseparent_obj'):
        model = cache.get('RExercisemodel')
        parent_obj = cache.get('RExerciseparent_obj')
    else:
        model = RExercise
        parent_obj = RExerciseParent
        cache.set('RExercisemodel', model)
        cache.set('RExerciseparent_obj', parent_obj)
    like_obj = RExerciseLike

    def get_context_data(self, **kwargs):
        context = super(RExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'R Exercise'
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


class CSharpExerciseView(View):
    def get(self, request):
        slug = CSharpExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:csharpexercisedetail', kwargs={'slug': slug}))


class CSharpExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('CSharpExercisemodel') and cache.get('CSharpExerciseparent_obj'):
        model = cache.get('CSharpExercisemodel')
        parent_obj = cache.get('CSharpExerciseparent_obj')
    else:
        model = CSharpExercise
        parent_obj = CSharpExerciseParent
        cache.set('CSharpExercisemodel', model)
        cache.set('CSharpExerciseparent_obj', parent_obj)
    like_obj = CSharpExerciseLike

    def get_context_data(self, **kwargs):
        context = super(CSharpExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'C# Exercise'
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


class SwiftExerciseView(View):
    def get(self, request):
        slug = SwiftExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:swiftexercisedetail', kwargs={'slug': slug}))


class SwiftExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('SwiftExercisemodel') and cache.get('SwiftExerciseparent_obj'):
        model = cache.get('SwiftExercisemodel')
        parent_obj = cache.get('SwiftExerciseparent_obj')
    else:
        model = SwiftExercise
        parent_obj = SwiftExerciseParent
        cache.set('SwiftExercisemodel', model)
        cache.set('SwiftExerciseparent_obj', parent_obj)
    like_obj = SwiftExerciseLike

    def get_context_data(self, **kwargs):
        context = super(SwiftExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Swift Exercise'
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


class JavaScriptExerciseView(View):
    def get(self, request):
        slug = JavaScriptExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:javascriptexercisedetail', kwargs={'slug': slug}))


class JavaScriptExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('JavaScriptExercisemodel') and cache.get('JavaScriptExerciseparent_obj'):
        model = cache.get('JavaScriptExercisemodel')
        parent_obj = cache.get('JavaScriptExerciseparent_obj')
    else:
        model = JavaScriptExercise
        parent_obj = JavaScriptExerciseParent
        cache.set('JavaScriptExercisemodel', model)
        cache.set('JavaScriptExerciseparent_obj', parent_obj)
    like_obj = JavaScriptExerciseLike

    def get_context_data(self, **kwargs):
        context = super(JavaScriptExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'JavaScript Exercise'
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


class PHPExerciseView(View):
    def get(self, request):
        slug = PHPExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:phpexercisedetail', kwargs={'slug': slug}))


class PHPExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('PHPExercisemodel') and cache.get('PHPExerciseparent_obj'):
        model = cache.get('PHPExercisemodel')
        parent_obj = cache.get('PHPExerciseparent_obj')
    else:
        model = PHPExercise
        parent_obj = PHPExerciseParent
        cache.set('PHPExercisemodel', model)
        cache.set('PHPExerciseparent_obj', parent_obj)
    like_obj = PHPExerciseLike

    def get_context_data(self, **kwargs):
        context = super(PHPExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'PHP Exercise'
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


class DotNetExerciseView(View):
    def get(self, request):
        slug = DotNetExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:dotnetexercisedetail', kwargs={'slug': slug}))


class DotNetExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    if cache.get('DotNetExercisemodel') and cache.get('DotNetExerciseparent_obj'):
        model = cache.get('DotNetExercisemodel')
        parent_obj = cache.get('DotNetExerciseparent_obj')
    else:
        model = DotNetExercise
        parent_obj = DotNetExerciseParent
        cache.set('DotNetExercisemodel', model)
        cache.set('DotNetExerciseparent_obj', parent_obj)
    like_obj = DotNetExerciseLike

    def get_context_data(self, **kwargs):
        context = super(DotNetExerciseDetailView, self).get_context_data(**kwargs)
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
        context['title'] = '.NET Exercise'
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
