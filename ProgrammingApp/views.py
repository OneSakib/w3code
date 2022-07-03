from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import View, DetailView
from .models import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order


# Create your views here.
class CView(View):
    def get(self, request):
        slug = CLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:cdetail', kwargs={'slug': slug}))


class CLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = CLanguage

    def get_context_data(self, **kwargs):
        context = super(CLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C Language'
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


class CPlusView(View):
    def get(self, request):
        slug = CplusLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:cplusdetail', kwargs={'slug': slug}))


class CPlusLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = CplusLanguage

    def get_context_data(self, **kwargs):
        context = super(CPlusLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C++ Language'
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



class PythonView(View):
    def get(self, request):
        slug = PythonLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:pythondetail', kwargs={'slug': slug}))


class PythonLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = PythonLanguage

    def get_context_data(self, **kwargs):
        context = super(PythonLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Python Language'
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



class JavaView(View):
    def get(self, request):
        slug = JavaLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:javadetail', kwargs={'slug': slug}))


class JavaLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = JavaLanguage

    def get_context_data(self, **kwargs):
        context = super(JavaLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java Language'
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



class AndroidView(View):
    def get(self, request):
        slug = AndroidLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:androiddetail', kwargs={'slug': slug}))


class AndroidLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = AndroidLanguage

    def get_context_data(self, **kwargs):
        context = super(AndroidLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Android'
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



class KotlinView(View):
    def get(self, request):
        slug = KotlinLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:kotlindetail', kwargs={'slug': slug}))


class KotlinLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = KotlinLanguage

    def get_context_data(self, **kwargs):
        context = super(KotlinLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Kotlin'
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



class RView(View):
    def get(self, request):
        slug = RLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:rdetail', kwargs={'slug': slug}))


class RLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = RLanguage

    def get_context_data(self, **kwargs):
        context = super(RLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'R Language'
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



class CSharpView(View):
    def get(self, request):
        slug = CsharpLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:csharpdetail', kwargs={'slug': slug}))


class CSharpLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = CsharpLanguage

    def get_context_data(self, **kwargs):
        context = super(CSharpLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C# Language'
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



class SwiftView(View):
    def get(self, request):
        slug = SwiftLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:swiftdetail', kwargs={'slug': slug}))


class SwiftLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = SwiftLanguage

    def get_context_data(self, **kwargs):
        context = super(SwiftLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Swift Language'
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



class JavaScriptView(View):
    def get(self, request):
        slug = JavaScriptLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:javascriptdetail', kwargs={'slug': slug}))


class JavaScriptLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = JavaScriptLanguage

    def get_context_data(self, **kwargs):
        context = super(JavaScriptLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        print(obj_list)
        context['title'] = 'JavaScript'
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


class PHPView(View):
    def get(self, request):
        slug = PHPLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:phpdetail', kwargs={'slug': slug}))


class PHPLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = PHPLanguage

    def get_context_data(self, **kwargs):
        context = super(PHPLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'PHP Language'
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


class DotNetView(View):
    def get(self, request):
        slug = DotNetLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:dotnetdetail', kwargs={'slug': slug}))


class DotNetLanguageDetailView(DetailView):
    template_name = 'programming/detail.html'
    model = DotNetLanguage

    def get_context_data(self, **kwargs):
        context = super(DotNetLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = '.NET Language'
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

