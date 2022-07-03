from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order


# Create your views here.

class HtmlView(View):
    def get(self, request):
        slug = HTMLs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:htmldetail', kwargs={'slug': slug}))


class HTMLDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = HTMLs

    def get_context_data(self, **kwargs):
        context = super(HTMLDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'HTML'
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


class CSSView(View):
    def get(self, request):
        slug = CSSs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:cssdetail', kwargs={'slug': slug}))


class CSSDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = CSSs

    def get_context_data(self, **kwargs):
        context = super(CSSDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'CSS'
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



class LaravelView(View):
    def get(self, request):
        slug = Laravels.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:laraveldetail', kwargs={'slug': slug}))


class LaravelDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Laravels

    def get_context_data(self, **kwargs):
        context = super(LaravelDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Laravel'
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



class WordpressView(View):
    def get(self, request):
        slug = Wordpress.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:wordpressdetail', kwargs={'slug': slug}))


class WordpressDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Wordpress

    def get_context_data(self, **kwargs):
        context = super(WordpressDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Wordpress'
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



class JSONView(View):
    def get(self, request):
        slug = JSONs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:jsondetail', kwargs={'slug': slug}))


class JSONDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = JSONs

    def get_context_data(self, **kwargs):
        context = super(JSONDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'JSON'
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



class AJAXView(View):
    def get(self, request):
        slug = Ajaxs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:ajaxdetail', kwargs={'slug': slug}))


class AJAXDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Ajaxs

    def get_context_data(self, **kwargs):
        context = super(AJAXDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'AJAX'
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



class BootstrapView(View):
    def get(self, request):
        slug = Bootstraps.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Web:bootstrapdetail', kwargs={'slug': slug}))


class BootstrapDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Bootstraps

    def get_context_data(self, **kwargs):
        context = super(BootstrapDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Bootstrap'
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

