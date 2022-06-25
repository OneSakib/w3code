from django.shortcuts import HttpResponseRedirect
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy
from django.views.generic import View, DetailView


# Create your views here.
class CExerciseView(View):
    def get(self, request):
        slug = CExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:cexercisedetail', kwargs={'slug': slug}))


class CExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = CExercise

    def get_context_data(self, **kwargs):
        context = super(CExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C Exercise'
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


class CPlusExerciseView(View):
    def get(self, request):
        slug = CPlusExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:cplusexcisedetail', kwargs={'slug': slug}))


class CPlusExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = CPlusExercise

    def get_context_data(self, **kwargs):
        context = super(CPlusExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C++ Exercise'
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


class PythonExerciseView(View):
    def get(self, request):
        slug = PythonExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:pythonexercisedetail', kwargs={'slug': slug}))


class PythonExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = PythonExercise

    def get_context_data(self, **kwargs):
        context = super(PythonExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Python Exercise'
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


class JavaExerciseView(View):
    def get(self, request):
        slug = JavaExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:javaexercisedetail', kwargs={'slug': slug}))


class JavaExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = JavaExercise

    def get_context_data(self, **kwargs):
        context = super(JavaExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java Exercise'
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


class KotlinExerciseView(View):
    def get(self, request):
        slug = KotlinExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:kotlinexercisedetail', kwargs={'slug': slug}))


class KotlinExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = KotlinExercise

    def get_context_data(self, **kwargs):
        context = super(KotlinExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Kotlin Exercise'
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


class RExerciseView(View):
    def get(self, request):
        slug = RExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:rexercisedetail', kwargs={'slug': slug}))


class RExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = RExercise

    def get_context_data(self, **kwargs):
        context = super(RExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'R Exercise'
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


class CSharpExerciseView(View):
    def get(self, request):
        slug = CSharpExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:csharpexercisedetail', kwargs={'slug': slug}))


class CSharpExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = CSharpExercise

    def get_context_data(self, **kwargs):
        context = super(CSharpExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C# Exercise'
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


class SwiftExerciseView(View):
    def get(self, request):
        slug = SwiftExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:swiftexercisedetail', kwargs={'slug': slug}))


class SwiftExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = SwiftExercise

    def get_context_data(self, **kwargs):
        context = super(SwiftExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Swift Exercise'
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


class JavaScriptExerciseView(View):
    def get(self, request):
        slug = JavaScriptExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:javascriptexercisedetail', kwargs={'slug': slug}))


class JavaScriptExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = JavaScriptExercise

    def get_context_data(self, **kwargs):
        context = super(JavaScriptExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'JavaScript Exercise'
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


class PHPExerciseView(View):
    def get(self, request):
        slug = PHPExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:phpexercisedetail', kwargs={'slug': slug}))


class PHPExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = PHPExercise

    def get_context_data(self, **kwargs):
        context = super(PHPExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'PHP Exercise'
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


class DotNetExerciseView(View):
    def get(self, request):
        slug = DotNetExercise.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Exercise:dotnetexercisedetail', kwargs={'slug': slug}))


class DotNetExerciseDetailView(DetailView):
    template_name = 'exercise/detail.html'
    model = DotNetExercise

    def get_context_data(self, **kwargs):
        context = super(DotNetExerciseDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = '.NET Exercise'
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
