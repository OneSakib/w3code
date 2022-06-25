from django.shortcuts import HttpResponseRedirect
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy
from django.views.generic import View, DetailView


# Create your views here.
class CProjectsView(View):
    def get(self, request):
        slug = CProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:cprojectsdetail', kwargs={'slug': slug}))


class CProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = CProjects

    def get_context_data(self, **kwargs):
        context = super(CProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C Projects'
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


class CPlusProjectsView(View):
    def get(self, request):
        slug = CPlusProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:cplusprojectsdetail', kwargs={'slug': slug}))


class CPlusProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = CPlusProjects

    def get_context_data(self, **kwargs):
        context = super(CPlusProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C++ Projects'
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


class PythonProjectsView(View):
    def get(self, request):
        slug = PythonProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:pythonprojectsdetail', kwargs={'slug': slug}))


class PythonProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = PythonProjects

    def get_context_data(self, **kwargs):
        context = super(PythonProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Python Projects'
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


class JavaProjectsView(View):
    def get(self, request):
        slug = JavaProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:javaprojectsdetail', kwargs={'slug': slug}))


class JavaProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = JavaProjects

    def get_context_data(self, **kwargs):
        context = super(JavaProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java Projects'
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


class KotlinProjectsView(View):
    def get(self, request):
        slug = KotlinProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:kotlinprojectsdetail', kwargs={'slug': slug}))


class KotlinProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = KotlinProjects

    def get_context_data(self, **kwargs):
        context = super(KotlinProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Kotlin Projects'
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


class RProjectsView(View):
    def get(self, request):
        slug = RProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:rprojectsdetail', kwargs={'slug': slug}))


class RProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = RProjects

    def get_context_data(self, **kwargs):
        context = super(RProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'R Projects'
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


class CSharpProjectsView(View):
    def get(self, request):
        slug = CSharpProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:csharpprojectsdetail', kwargs={'slug': slug}))


class CSharpProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = CSharpProjects

    def get_context_data(self, **kwargs):
        context = super(CSharpProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C# Projects'
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


class SwiftProjectsView(View):
    def get(self, request):
        slug = SwiftProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:swiftprojectsdetail', kwargs={'slug': slug}))


class SwiftProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = SwiftProjects

    def get_context_data(self, **kwargs):
        context = super(SwiftProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Swift Projects'
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


class JavaScriptProjectsView(View):
    def get(self, request):
        slug = JavaScriptProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:javascriptprojectsdetail', kwargs={'slug': slug}))


class JavaScriptProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = JavaScriptProjects

    def get_context_data(self, **kwargs):
        context = super(JavaScriptProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'JavaScript Projects'
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


class PHPProjectsView(View):
    def get(self, request):
        slug = PHPProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:phpprojectsdetail', kwargs={'slug': slug}))


class PHPProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = PHPProjects

    def get_context_data(self, **kwargs):
        context = super(PHPProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'PHP Projects'
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


class AndroidProjectView(View):
    def get(self, request):
        slug = AndroidProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:androidprojectsdetail', kwargs={'slug': slug}))


class AndroidProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = PHPProjects

    def get_context_data(self, **kwargs):
        context = super(AndroidProjectDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Android Project'
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


class DotNetProjectsView(View):
    def get(self, request):
        slug = DotNetProjects.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Projects:androidprojectsdetail', kwargs={'slug': slug}))


class DotNetProjectsDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = DotNetProjects

    def get_context_data(self, **kwargs):
        context = super(DotNetProjectsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = '.NET Projects'
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
