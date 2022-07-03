from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from django.urls import reverse_lazy
from next_prev import prev_in_order, next_in_order


# Create your views here.

class ServletView(View):
    def get(self, request):
        slug = Servlets.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:servletdetail', kwargs={'slug': slug}))


class ServletDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Servlets

    def get_context_data(self, **kwargs):
        context = super(ServletDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Servlet'
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


class JspView(View):
    def get(self, request):
        slug = JSPs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:jspdetail', kwargs={'slug': slug}))


class JSPDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = JSPs

    def get_context_data(self, **kwargs):
        context = super(JSPDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'JSP'
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


class SpringBootView(View):
    def get(self, request):
        slug = SpringBoot.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:springbootdetail', kwargs={'slug': slug}))


class SpringBootDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = SpringBoot

    def get_context_data(self, **kwargs):
        context = super(SpringBootDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'SpringBoot'
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


class SpringFrameworkView(View):
    def get(self, request):
        slug = SpringFramework.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:springframeworkdetail', kwargs={'slug': slug}))


class SpringFrameworkDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = SpringFramework

    def get_context_data(self, **kwargs):
        context = super(SpringFrameworkDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Spring Framework'
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


class HibernateView(View):
    def get(self, request):
        slug = Hibernates.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:hibernatedetail', kwargs={'slug': slug}))


class HibernateDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Hibernates

    def get_context_data(self, **kwargs):
        context = super(HibernateDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java Hibernate'
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


class JavaSwingView(View):
    def get(self, request):
        slug = JavaSwings.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaswingdetail', kwargs={'slug': slug}))


class JavaSwingDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = JavaSwings

    def get_context_data(self, **kwargs):
        context = super(JavaSwingDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java Swing'
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


class JavaFXView(View):
    def get(self, request):
        slug = JavaFXs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javafxdetail', kwargs={'slug': slug}))


class JavaFxDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = JavaFXs

    def get_context_data(self, **kwargs):
        context = super(JavaFxDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'JavaFX'
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


class JavaAWTView(View):
    def get(self, request):
        slug = JavaAWT.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaawtdetail', kwargs={'slug': slug}))


class JavaAWTDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = JavaAWT

    def get_context_data(self, **kwargs):
        context = super(JavaAWTDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java AWT'
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


class JavaCollectionsView(View):
    def get(self, request):
        slug = Collections.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javacollectionsdetail', kwargs={'slug': slug}))


class JavaCollectionsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Collections

    def get_context_data(self, **kwargs):
        context = super(JavaCollectionsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java Collections'
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


class JavaDateView(View):
    def get(self, request):
        slug = JavaDate.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javadatedetail', kwargs={'slug': slug}))


class JavaDateDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = JavaDate

    def get_context_data(self, **kwargs):
        context = super(JavaDateDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java Date'
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


class JavaIOView(View):
    def get(self, request):
        slug = JavaIO.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaiodetail', kwargs={'slug': slug}))


class JavaIODetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = JavaIO

    def get_context_data(self, **kwargs):
        context = super(JavaIODetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Java I/O'
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
