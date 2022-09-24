from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from django.urls import reverse_lazy
from next_prev import prev_in_order, next_in_order
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *


# Create your views here.

class ServletView(View):
    def get(self, request):
        slug = Servlets.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:servletdetail', kwargs={'slug': slug}))


class ServletDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Servletsmodel') and cache.get('Servletsparent_obj'):
        model = cache.get('Servletsmodel')
        parent_obj = cache.get('Servletsparent_obj')
    else:
        model = Servlets
        parent_obj = ServletsParent
        cache.set('Servletsmodel', model)
        cache.set('Servletsparent_obj', parent_obj)
    like_obj = ServletsLike

    def get_context_data(self, **kwargs):
        context = super(ServletDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Servlet'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class JspView(View):
    def get(self, request):
        slug = JSPs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:jspdetail', kwargs={'slug': slug}))


class JSPDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('JSPsmodel') and cache.get('JSPsparent_obj'):
        model = cache.get('JSPsmodel')
        parent_obj = cache.get('JSPsparent_obj')
    else:
        model = JSPs
        parent_obj = JSPsParent
        cache.set('JSPsmodel', model)
        cache.set('JSPsparent_obj', parent_obj)
    like_obj = JSPsLike

    def get_context_data(self, **kwargs):
        context = super(JSPDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'JSP'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class SpringBootView(View):
    def get(self, request):
        slug = SpringBoot.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:springbootdetail', kwargs={'slug': slug}))


class SpringBootDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('SpringBootmodel') and cache.get('SpringBootparent_obj'):
        model = cache.get('SpringBootmodel')
        parent_obj = cache.get('SpringBootparent_obj')
    else:
        model = SpringBoot
        parent_obj = SpringBootParent
        cache.set('SpringBootmodel', model)
        cache.set('SpringBootparent_obj', parent_obj)
    like_obj = SpringBootLike

    def get_context_data(self, **kwargs):
        context = super(SpringBootDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'SpringBoot'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class SpringFrameworkView(View):
    def get(self, request):
        slug = SpringFramework.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:springframeworkdetail', kwargs={'slug': slug}))


class SpringFrameworkDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('SpringFrameworkmodel') and cache.get('SpringFrameworkparent_obj'):
        model = cache.get('SpringFrameworkmodel')
        parent_obj = cache.get('SpringFrameworkparent_obj')
    else:
        model = SpringFramework
        parent_obj = SpringBootParent
        cache.set('SpringFrameworkmodel', model)
        cache.set('SpringFrameworkparent_obj', parent_obj)
    like_obj = SpringFrameworkLike

    def get_context_data(self, **kwargs):
        context = super(SpringFrameworkDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Spring Framework'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class HibernateView(View):
    def get(self, request):
        slug = Hibernates.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:hibernatedetail', kwargs={'slug': slug}))


class HibernateDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Hibernatesmodel') and cache.get('Hibernatesparent_obj'):
        model = cache.get('Hibernatesmodel')
        parent_obj = cache.get('Hibernatesparent_obj')
    else:
        model = Hibernates
        parent_obj = HibernatesParent
        cache.set('Hibernatesmodel', model)
        cache.set('Hibernatesparent_obj', parent_obj)
    like_obj = HibernatesLike

    def get_context_data(self, **kwargs):
        context = super(HibernateDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Java Hibernate'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class JavaSwingView(View):
    def get(self, request):
        slug = JavaSwings.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaswingdetail', kwargs={'slug': slug}))


class JavaSwingDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('JavaSwingsmodel') and cache.get('JavaSwingsparent_obj'):
        model = cache.get('JavaSwingsmodel')
        parent_obj = cache.get('JavaSwingsparent_obj')
    else:
        model = JavaSwings
        parent_obj = JavaSwingsParent
        cache.set('JavaSwingsmodel', model)
        cache.set('JavaSwingsparent_obj', parent_obj)
    like_obj = JavaSwingsLike

    def get_context_data(self, **kwargs):
        context = super(JavaSwingDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Java Swing'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class JavaFXView(View):
    def get(self, request):
        slug = JavaFXs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javafxdetail', kwargs={'slug': slug}))


class JavaFxDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('JavaFXsmodel') and cache.get('JavaFXsparent_obj'):
        model = cache.get('JavaFXsmodel')
        parent_obj = cache.get('JavaFXsparent_obj')
    else:
        model = JavaFXs
        parent_obj = JavaFXsParent
        cache.set('JavaFXsmodel', model)
        cache.set('JavaFXsparent_obj', parent_obj)
    like_obj = JavaFXsLike

    def get_context_data(self, **kwargs):
        context = super(JavaFxDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'JavaFX'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class JavaAWTView(View):
    def get(self, request):
        slug = JavaAWT.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaawtdetail', kwargs={'slug': slug}))


class JavaAWTDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('JavaAWTmodel') and cache.get('JavaAWTparent_obj'):
        model = cache.get('JavaAWTmodel')
        parent_obj = cache.get('JavaAWTparent_obj')
    else:
        model = JavaAWT
        parent_obj = JavaAWTParent
        cache.set('JavaAWTmodel', model)
        cache.set('JavaAWTparent_obj', parent_obj)
    like_obj = JavaAWTLike

    def get_context_data(self, **kwargs):
        context = super(JavaAWTDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Java AWT'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context


class JavaCollectionsView(View):
    def get(self, request):
        slug = Collections.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javacollectionsdetail', kwargs={'slug': slug}))


class JavaCollectionsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Collectionsmodel') and cache.get('Collectionsparent_obj'):
        model = cache.get('Collectionsmodel')
        parent_obj = cache.get('Collectionsparent_obj')
    else:
        model = Collections
        parent_obj = CollectionsParent
        cache.set('Collectionsmodel', model)
        cache.set('Collectionsparent_obj', parent_obj)
    like_obj = CollectionsLike

    def get_context_data(self, **kwargs):
        context = super(JavaCollectionsDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Java Collections'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class JavaDateView(View):
    def get(self, request):
        slug = JavaDate.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javadatedetail', kwargs={'slug': slug}))


class JavaDateDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('JavaDatemodel') and cache.get('JavaDateparent_obj'):
        model = cache.get('JavaDatemodel')
        parent_obj = cache.get('JavaDateparent_obj')
    else:
        model = JavaDate
        parent_obj = JavaDateParent
        cache.set('JavaDatemodel', model)
        cache.set('JavaDateparent_obj', parent_obj)
    like_obj = JavaDateLike

    def get_context_data(self, **kwargs):
        context = super(JavaDateDetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Java Date'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)


class JavaIOView(View):
    def get(self, request):
        slug = JavaIO.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Java:javaiodetail', kwargs={'slug': slug}))


class JavaIODetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('JavaIOmodel') and cache.get('JavaIOparent_obj'):
        model = cache.get('JavaIOmodel')
        parent_obj = cache.get('JavaIOparent_obj')
    else:
        model = JavaIO
        parent_obj = JavaIOParent
        cache.set('JavaIOmodel', model)
        cache.set('JavaIOparent_obj', parent_obj)
    like_obj = JavaIOLike

    def get_context_data(self, **kwargs):
        context = super(JavaIODetailView, self).get_context_data(**kwargs)
        obj_list = self.parent_obj.objects.all()
        context['obj_list'] = obj_list
        # Like Button
        context['obj_like_count'] = self.like_obj.objects.all().count()
        if self.request.user.is_authenticated:
            user = User.objects.get(username=self.request.user)
            if self.like_obj.objects.filter(user=user, post=self.object).exists():
                context['obj_like_exist'] = "Yes"
        else:
            context['obj_like_exist'] = "No"
        context['title'] = 'Java I/O'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, **kwargs):
        pk = request.POST.get('pk')
        user = User.objects.get(username=request.user)
        context = {}
        if self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk)).exists():
            o = self.like_obj.objects.filter(user=user, post=self.model.objects.get(pk=pk))
            o.delete()
            context['ok'] = 'delete'
        else:
            self.like_obj.objects.create(user=user, post=self.model.objects.get(pk=pk))
            context['ok'] = 'create'
        context['number'] = self.like_obj.objects.all().count()
        return JsonResponse(context)
