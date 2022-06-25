from django.shortcuts import HttpResponseRedirect
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy
from django.views.generic import View, DetailView


# Create your views here.
class CProgrammeView(View):
    def get(self, request):
        slug = CProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:cprogrammedetail', kwargs={'slug': slug}))


class CProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = CProgramme

    def get_context_data(self, **kwargs):
        context = super(CProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C Programme'
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


class CPlusProgrammeView(View):
    def get(self, request):
        slug = CPlusProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:cplusprogrammedetail', kwargs={'slug': slug}))


class CPlusProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = CPlusProgramme

    def get_context_data(self, **kwargs):
        context = super(CPlusProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C++ Programme'
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


class PythonProgrammeView(View):
    def get(self, request):
        slug = PythonProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:pythonprogrammedetail', kwargs={'slug': slug}))


class PythonProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = PythonProgramme

    def get_context_data(self, **kwargs):
        context = super(PythonProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Python Programme'
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


class JavaProgrammeView(View):
    def get(self, request):
        slug = JavaProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:javaprogrammedetail', kwargs={'slug': slug}))


class JavaProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = JavaProgramme

    def get_context_data(self, **kwargs):
        context = super(JavaProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java Programme'
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


class KotlinProgrammeView(View):
    def get(self, request):
        slug = KotlinProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:kotlinprogrammedetail', kwargs={'slug': slug}))


class KotlinProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = KotlinProgramme

    def get_context_data(self, **kwargs):
        context = super(KotlinProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Kotlin Programme'
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


class RProgrammeView(View):
    def get(self, request):
        slug = RProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:rprogrammedetail', kwargs={'slug': slug}))


class RProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = RProgramme

    def get_context_data(self, **kwargs):
        context = super(RProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'R Programme'
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


class CSharpProgrammeView(View):
    def get(self, request):
        slug = CSharpProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:csharpprogrammedetail', kwargs={'slug': slug}))


class CSharpProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = CSharpProgramme

    def get_context_data(self, **kwargs):
        context = super(CSharpProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'C# Programme'
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


class SwiftProgrammeView(View):
    def get(self, request):
        slug = SwiftProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:swiftprogrammedetail', kwargs={'slug': slug}))


class SwiftProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = SwiftProgramme

    def get_context_data(self, **kwargs):
        context = super(SwiftProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Swift Programme'
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


class JavaScriptProgrammeView(View):
    def get(self, request):
        slug = JavaScriptProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:javascriptprogrammedetail', kwargs={'slug': slug}))


class JavaScriptProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = JavaScriptProgramme

    def get_context_data(self, **kwargs):
        context = super(JavaScriptProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'JavaScript Programme'
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


class PHPProgrammeView(View):
    def get(self, request):
        slug = PHPProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:phpprogrammedetail', kwargs={'slug': slug}))


class PHPProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = PHPProgramme

    def get_context_data(self, **kwargs):
        context = super(PHPProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'PHP Programme'
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


class DotNetProgrammeView(View):
    def get(self, request):
        slug = DotNetProgramme.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programme:dotnetprogrammedetail', kwargs={'slug': slug}))


class DotNetProgrammeDetailView(DetailView):
    template_name = 'programme/detail.html'
    model = DotNetProgramme

    def get_context_data(self, **kwargs):
        context = super(DotNetProgrammeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = '.NET Programme'
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
