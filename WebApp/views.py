from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, FormView, DetailView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order


# Create your views here.

class HtmlView(View):
    def get(self, request):
        slug = HTMLs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:htmldetail', kwargs={'slug': slug}))


class HTMLDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = HTMLsCommentsForm
    model = HTMLs

    def get_context_data(self, **kwargs):
        context = super(HTMLDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = HTMLsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Web:htmldetail', kwargs={'slug': self.kwargs['slug']}))


class CSSView(View):
    def get(self, request):
        slug = CSSs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:cssdetail', kwargs={'slug': slug}))


class CSSDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = CSSsCommentsForm
    model = CSSs

    def get_context_data(self, **kwargs):
        context = super(CSSDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = CSSsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Web:cssdetail', kwargs={'slug': self.kwargs['slug']}))


class LaravelView(View):
    def get(self, request):
        slug = Laravels.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:laraveldetail', kwargs={'slug': slug}))


class LaravelDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = LaravelsCommentsForm
    model = Laravels

    def get_context_data(self, **kwargs):
        context = super(LaravelsCommentsForm, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = LaravelsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Web:laraveldetail', kwargs={'slug': self.kwargs['slug']}))


class WordpressView(View):
    def get(self, request):
        slug = Wordpress.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:wordpressdetail', kwargs={'slug': slug}))


class WordpressDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = WordpressCommentsForm
    model = Wordpress

    def get_context_data(self, **kwargs):
        context = super(WordpressDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = WordpressComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Web:wordpressdetail', kwargs={'slug': self.kwargs['slug']}))


class JSONView(View):
    def get(self, request):
        slug = JSONs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:jsondetail', kwargs={'slug': slug}))


class JSONDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = JSONsCommentsForm
    model = JSONs

    def get_context_data(self, **kwargs):
        context = super(JSONDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JSONsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Web:jsondetail', kwargs={'slug': self.kwargs['slug']}))


class AJAXView(View):
    def get(self, request):
        slug = Ajaxs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:ajaxdetail', kwargs={'slug': slug}))


class AJAXDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = AjaxsCommentsForm
    model = Ajaxs

    def get_context_data(self, **kwargs):
        context = super(AJAXDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = AjaxsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Web:ajaxdetail', kwargs={'slug': self.kwargs['slug']}))


class BootstrapView(View):
    def get(self, request):
        slug = Bootstraps.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:bootstrapdetail', kwargs={'slug': slug}))


class BootstrapDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = BootstrapsCommentsForm
    model = Bootstraps

    def get_context_data(self, **kwargs):
        context = super(BootstrapDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = BootstrapsComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Web:bootstrapdetail', kwargs={'slug': self.kwargs['slug']}))
