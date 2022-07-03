from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from django.urls import reverse_lazy
from next_prev import prev_in_order, next_in_order
from .models import *


# Create your views here.
class JqueryView(View):
    def get(self, request):
        slug = Jquery.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:jquerydetail', kwargs={'slug': slug}))


class JqueryDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Jquery

    def get_context_data(self, **kwargs):
        context = super(JqueryDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'JQuery'
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


class AngularView(View):
    def get(self, request):
        slug = Angularjs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:angulardetail', kwargs={'slug': slug}))


class AngularDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Angularjs

    def get_context_data(self, **kwargs):
        context = super(AngularDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'AngularJs'
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


class NodejsView(View):
    def get(self, request):
        slug = Nodejs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:nodejsdetail', kwargs={'slug': slug}))


class NodejsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Nodejs

    def get_context_data(self, **kwargs):
        context = super(NodejsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'NodeJs'
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


class ExpressjsView(View):
    def get(self, request):
        slug = Expressjs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:expressjsdetail', kwargs={'slug': slug}))


class ExpressjsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Expressjs

    def get_context_data(self, **kwargs):
        context = super(ExpressjsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'ExpressJs'
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


class ReactjsView(View):
    def get(self, request):
        slug = Reactjs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:reactjsdetail', kwargs={'slug': slug}))


class ReactjsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Reactjs

    def get_context_data(self, **kwargs):
        context = super(ReactjsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'ReactJS'
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


class TypescriptView(View):
    def get(self, request):
        slug = TypeScripts.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:typescriptdetail', kwargs={'slug': slug}))


class TypescriptDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = TypeScripts

    def get_context_data(self, **kwargs):
        context = super(TypescriptDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'TypeScript'
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


class VuejsView(View):
    def get(self, request):
        slug = VUEjs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('JavaScript:vuejsdetail', kwargs={'slug': slug}))


class VuejsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = VUEjs

    def get_context_data(self, **kwargs):
        context = super(VuejsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'VUEJS'
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
