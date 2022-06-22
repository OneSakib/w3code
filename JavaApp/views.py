from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView, FormView
from .forms import *
from django.urls import reverse_lazy
from next_prev import prev_in_order, next_in_order


# Create your views here.

class ServletView(View):
    def get(self, request):
        slug = Servlets.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:servletdetail', kwargs={'slug': slug}))


class ServletDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = ServletsCommentsForm
    model = Servlets

    def get_context_data(self, **kwargs):
        context = super(ServletDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = ServletsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:servletdetail', kwargs={'slug': self.kwargs['slug']}))


class JspView(View):
    def get(self, request):
        slug = JSPs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:jspdetail', kwargs={'slug': slug}))


class JSPDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = JSPsCommentsForm
    model = JSPs

    def get_context_data(self, **kwargs):
        context = super(JSPDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JSPsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:jspdetail', kwargs={'slug': self.kwargs['slug']}))


class SpringBootView(View):
    def get(self, request):
        slug = SpringBoot.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:springbootdetail', kwargs={'slug': slug}))


class SpringBootDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = SpringBootCommentsForm
    model = SpringBoot

    def get_context_data(self, **kwargs):
        context = super(SpringBootDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = SpringBootComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:springbootdetail', kwargs={'slug': self.kwargs['slug']}))


class SpringFrameworkView(View):
    def get(self, request):
        slug = SpringFramework.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:springframeworkdetail', kwargs={'slug': slug}))


class SpringFrameworkDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = SpringBootCommentsForm
    model = SpringFramework

    def get_context_data(self, **kwargs):
        context = super(SpringFrameworkDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = SpringFrameworkComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:springframeworkdetail', kwargs={'slug': self.kwargs['slug']}))


class HibernateView(View):
    def get(self, request):
        slug = Hibernates.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:hibernatedetail', kwargs={'slug': slug}))


class HibernateDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = HibernatesCommentsForm
    model = Hibernates

    def get_context_data(self, **kwargs):
        context = super(HibernateDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = HibernatesComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:hibernatedetail', kwargs={'slug': self.kwargs['slug']}))


class JavaSwingView(View):
    def get(self, request):
        slug = JavaSwings.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaswingdetail', kwargs={'slug': slug}))


class JavaSwingDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = JavaSwingsCommentsForm
    model = JavaSwings

    def get_context_data(self, **kwargs):
        context = super(JavaSwingDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JavaSwingsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:javaswingdetail', kwargs={'slug': self.kwargs['slug']}))


class JavaFXView(View):
    def get(self, request):
        slug = JavaFXs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javafxdetail', kwargs={'slug': slug}))


class JavaFxDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = JavaFXsCommentsForm
    model = JavaFXs

    def get_context_data(self, **kwargs):
        context = super(JavaFxDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JavaFXsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:javafxdetail', kwargs={'slug': self.kwargs['slug']}))


class JavaAWTView(View):
    def get(self, request):
        slug = JavaAWT.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaawtdetail', kwargs={'slug': slug}))


class JavaAWTDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = JavaAWTCommentsForm
    model = JavaAWT

    def get_context_data(self, **kwargs):
        context = super(JavaAWTDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JavaAWT.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:javaawtdetail', kwargs={'slug': self.kwargs['slug']}))


class JavaCollectionsView(View):
    def get(self, request):
        slug = Collections.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javacollectionsdetail', kwargs={'slug': slug}))


class JavaCollectionsDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = CollectionsCommentsForm
    model = Collections

    def get_context_data(self, **kwargs):
        context = super(JavaCollectionsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = CollectionsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:javacollectionsdetail', kwargs={'slug': self.kwargs['slug']}))


class JavaDateView(View):
    def get(self, request):
        slug = JavaDate.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javadatedetail', kwargs={'slug': slug}))


class JavaDateDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = JavaDateCommentsForm
    model = JavaDate

    def get_context_data(self, **kwargs):
        context = super(JavaDateDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JavaDateComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:javadatedetail', kwargs={'slug': self.kwargs['slug']}))


class JavaIOView(View):
    def get(self, request):
        slug = JavaIO.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaiodetail', kwargs={'slug': slug}))


class JavaIODetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = JavaIOCommentsForm
    model = JavaIO

    def get_context_data(self, **kwargs):
        context = super(JavaIODetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JavaIOCommentsForm.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Java:javaiodetail', kwargs={'slug': self.kwargs['slug']}))
