from django.shortcuts import HttpResponseRedirect, render
from django.views.generic import View, FormView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order


# Create your views here.
class CView(View):
    def get(self, request):
        slug = CLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:cdetail', kwargs={'slug': slug}))


class CLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = CLanguageCommentsForm
    model = CLanguage

    def get_context_data(self, **kwargs):
        context = super(CLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = CLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:cdetail', kwargs={'slug': self.kwargs['slug']}))


class CPlusView(View):
    def get(self, request):
        slug = CplusLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:cplusdetail', kwargs={'slug': slug}))


class CPlusLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = CplusLanguageCommentsForm
    model = CplusLanguage

    def get_context_data(self, **kwargs):
        context = super(CPlusLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = CplusLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:cplusdetail', kwargs={'slug': self.kwargs['slug']}))


class PythonView(View):
    def get(self, request):
        slug = PythonLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:pythondetail', kwargs={'slug': slug}))


class PythonLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = PythonLanguageCommentsForm
    model = PythonLanguage

    def get_context_data(self, **kwargs):
        context = super(PythonLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = PythonLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:pythondetail', kwargs={'slug': self.kwargs['slug']}))


class JavaView(View):
    def get(self, request):
        slug = JavaLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:javadetail', kwargs={'slug': slug}))


class JavaLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = JavaLanguageCommentsForm
    model = JavaLanguage

    def get_context_data(self, **kwargs):
        context = super(JavaLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JavaLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:javadetail', kwargs={'slug': self.kwargs['slug']}))


class AndroidView(View):
    def get(self, request):
        slug = AndroidLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:androiddetail', kwargs={'slug': slug}))


class AndroidLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = AndroidLanguageCommentsForm
    model = AndroidLanguage

    def get_context_data(self, **kwargs):
        context = super(AndroidLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = AndroidLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:androiddetail', kwargs={'slug': self.kwargs['slug']}))


class KotlinView(View):
    def get(self, request):
        slug = KotlinLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:kotlindetail', kwargs={'slug': slug}))


class KotlinLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = KotlinLanguageCommentsForm
    model = KotlinLanguage

    def get_context_data(self, **kwargs):
        context = super(KotlinLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = KotlinLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:kotlindetail', kwargs={'slug': self.kwargs['slug']}))


class RView(View):
    def get(self, request):
        slug = RLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:rdetail', kwargs={'slug': slug}))


class RLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = RLanguageCommentsForm
    model = RLanguage

    def get_context_data(self, **kwargs):
        context = super(RLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = RLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:rdetail', kwargs={'slug': self.kwargs['slug']}))


class CSharpView(View):
    def get(self, request):
        slug = CsharpLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:csharpdetail', kwargs={'slug': slug}))


class CSharpLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = CsharpLanguageCommentsForm
    model = CsharpLanguage

    def get_context_data(self, **kwargs):
        context = super(CSharpLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = CsharpLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:csharpdetail', kwargs={'slug': self.kwargs['slug']}))


class SwiftView(View):
    def get(self, request):
        slug = SwiftLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:swiftdetail', kwargs={'slug': slug}))


class SwiftLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = SwiftLanguageCommentsForm
    model = SwiftLanguage

    def get_context_data(self, **kwargs):
        context = super(SwiftLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = SwiftLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:swiftdetail', kwargs={'slug': self.kwargs['slug']}))


class JavaScriptView(View):
    def get(self, request):
        slug = JavaScriptLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:javascriptdetail', kwargs={'slug': slug}))


class JavaScriptLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = JavaScriptLanguageCommentsForm
    model = JavaScriptLanguage

    def get_context_data(self, **kwargs):
        context = super(JavaScriptLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        print(obj_list)
        context['comments'] = JavaScriptLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:javascriptdetail', kwargs={'slug': self.kwargs['slug']}))


class PHPView(View):
    def get(self, request):
        slug = PHPLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:phpdetail', kwargs={'slug': slug}))


class PHPLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = PHPLanguageCommentsForm
    model = PHPLanguage

    def get_context_data(self, **kwargs):
        context = super(PHPLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = PHPLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:phpdetail', kwargs={'slug': self.kwargs['slug']}))


class DotNetView(View):
    def get(self, request):
        slug = DotNetLanguage.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Programming:dotnetdetail', kwargs={'slug': slug}))


class DotNetLanguageDetailView(DetailView, FormView):
    template_name = 'programming/detail.html'
    form_class = DotNetLanguageCommentsForm
    model = DotNetLanguage

    def get_context_data(self, **kwargs):
        context = super(DotNetLanguageDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DotNetLanguageComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Programming:dotnetdetail', kwargs={'slug': self.kwargs['slug']}))
