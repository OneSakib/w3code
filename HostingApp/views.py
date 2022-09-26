from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, FormView, View
from .forms import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import get_object_pagination


# Create your views here.
class DigitalOceanView(View):
    def get(self, request):
        slug = DigitalOcean.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:digitaloceandetail', kwargs={'slug': slug}))


class DigitalOceanDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DigitalOceanCommentsForm
    if cache.get('DigitalOceanmodel') and cache.get('DigitalOceanparent_obj'):
        model = cache.get('DigitalOceanmodel')
        parent_obj = cache.get('DigitalOceanparent_obj')

    else:
        model = DigitalOcean
        parent_obj = DigitalOceanParent
        cache.set('DigitalOceanmodel', model)
        cache.set('DigitalOceanparent_obj', parent_obj)

    like_obj = DigitalOceanLike

    def get_context_data(self, **kwargs):
        context = super(DigitalOceanDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = DigitalOceanComments.objects.filter(post=self.object)
        context['title'] = 'DigitalOcean'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(
                reverse_lazy('Hosting:digitaloceandetail', kwargs={'slug': self.kwargs['slug']}))
        else:
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


class MSAzureView(View):
    def get(self, request):
        slug = MSAzure.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:msazuredetail', kwargs={'slug': slug}))


class MSAzureDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = MSAzureCommentsForm
    if cache.get('MSAzuremodel') and cache.get('MSAzureparent_obj'):
        model = cache.get('MSAzuremodel')
        parent_obj = cache.get('MSAzureparent_obj')
    else:
        model = MSAzure
        parent_obj = MSAzureParent
        cache.set('MSAzuremodel', model)
        cache.set('MSAzureparent_obj', parent_obj)
    like_obj = MSAzureLike

    def get_context_data(self, **kwargs):
        context = super(MSAzureDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = MSAzureComments.objects.filter(post=self.object)
        context['title'] = 'MSAzure'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:msazuredetail', kwargs={'slug': self.kwargs['slug']}))
        else:
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


class AWSView(View):
    def get(self, request):
        slug = AWS.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:awsdetail', kwargs={'slug': slug}))


class AWSDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = AWSCommentsForm
    if cache.get('AWSmodel') and cache.get('AWSparent_obj'):
        model = cache.get('AWSmodel')
        parent_obj = cache.get('AWSparent_obj')
    else:
        model = AWS
        parent_obj = AWSParent
        cache.set('AWSmodel', model)
        cache.set('AWSparent_obj', parent_obj)
    like_obj = AWSLike

    def get_context_data(self, **kwargs):
        context = super(AWSDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = AWSComments.objects.filter(post=self.object)
        context['title'] = 'AWS'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:awsdetail', kwargs={'slug': self.kwargs['slug']}))

        else:
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


class PythonAnywhereView(View):
    def get(self, request):
        slug = PythonAnywhere.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:pythonanywheredetail', kwargs={'slug': slug}))


class PythonAnywhereDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = PythonAnywhereCommentsForm
    if cache.get('PythonAnywheremodel') and cache.get('PythonAnywhereparent_obj'):
        model = cache.get('PythonAnywheremodel')
        parent_obj = cache.get('PythonAnywhereparent_obj')
    else:
        model = PythonAnywhere
        parent_obj = PythonAnywhereParent
        cache.set('PythonAnywheremodel', model)
        cache.set('PythonAnywhereparent_obj', parent_obj)
    like_obj = PythonAnywhereLike

    def get_context_data(self, **kwargs):
        context = super(PythonAnywhereDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = PythonAnywhereComments.objects.filter(post=self.object)
        context['title'] = 'PythonAnywhere'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(
                reverse_lazy('Hosting:pythonanywheredetail', kwargs={'slug': self.kwargs['slug']}))
        else:
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


class HerokuAppView(View):
    def get(self, request):
        slug = HerokuApp.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:herokuappdetail', kwargs={'slug': slug}))


class HerokuAppDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = HerokuAppCommentsForm
    if cache.get('HerokuAppmodel') and cache.get('HerokuAppparent_obj'):
        model = cache.get('HerokuAppmodel')
        parent_obj = cache.get('HerokuAppparent_obj')
    else:
        model = HerokuApp
        parent_obj = HerokuAppParent
        cache.set('HerokuAppmodel', model)
        cache.set('HerokuAppparent_obj', parent_obj)
    like_obj = HerokuAppLike

    def get_context_data(self, **kwargs):
        context = super(HerokuAppDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = HerokuAppComments.objects.filter(post=self.object)
        context['title'] = 'HerokuApp'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:herokuappdetail', kwargs={'slug': self.kwargs['slug']}))
        else:
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


class GithubHostView(View):
    def get(self, request):
        slug = GithubHost.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:githubhostdetail', kwargs={'slug': slug}))


class GithubHostDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = GithubHostCommentsForm
    if cache.get('GithubHostmodel') and cache.get('GithubHostparent_obj'):
        model = cache.get('GithubHostmodel')
        parent_obj = cache.get('GithubHostparent_obj')
    else:
        model = GithubHost
        parent_obj = GithubHostParent
        cache.set('GithubHostmodel', model)
        cache.set('GithubHostparent_obj', parent_obj)
    like_obj = GithubHostLike

    def get_context_data(self, **kwargs):
        context = super(GithubHostDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = GithubHostComments.objects.filter(post=self.object)
        context['title'] = 'GithubHost'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:githubhostdetail', kwargs={'slug': self.kwargs['slug']}))
        else:
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


class BlueHostView(View):
    def get(self, request):
        slug = BlueHost.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:bluehostdetail', kwargs={'slug': slug}))


class BlueHostDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = BlueHostCommentsForm
    if cache.get('BlueHostmodel') and cache.get('BlueHostparent_obj'):
        model = cache.get('BlueHostmodel')
        parent_obj = cache.get('BlueHostparent_obj')
    else:
        model = BlueHost
        parent_obj = BlueHostParent
        cache.set('BlueHostmodel', model)
        cache.set('BlueHostparent_obj', parent_obj)
    like_obj = BlueHostLike

    def get_context_data(self, **kwargs):
        context = super(BlueHostDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = BlueHostComments.objects.filter(post=self.object)
        context['title'] = 'BlueHost'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:bluehostdetail', kwargs={'slug': self.kwargs['slug']}))

        else:
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


class HostGatorView(View):
    def get(self, request):
        slug = HostGator.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:hostgatordetail', kwargs={'slug': slug}))


class HostGatorDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = HostGatorCommentsForm
    if cache.get('HostGatormodel') and cache.get('HostGatorparent_obj'):
        model = cache.get('HostGatormodel')
        parent_obj = cache.get('HostGatorparent_obj')
    else:
        model = HostGator
        parent_obj = HostGatorParent
        cache.set('HostGatormodel', model)
        cache.set('HostGatorparent_obj', parent_obj)
    like_obj = HostGatorLike

    def get_context_data(self, **kwargs):
        context = super(HostGatorDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = HostGatorComments.objects.filter(post=self.object)
        context['title'] = 'HostGator'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:hostgatordetail', kwargs={'slug': self.kwargs['slug']}))
        else:
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


class InMotionHostingView(View):
    def get(self, request):
        slug = InMotionHosting.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:inmotionhostingdetail', kwargs={'slug': slug}))


class InMotionHostingDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = InMotionHostingCommentsForm
    if cache.get('InMotionHostingmodel') and cache.get('InMotionHostingparent_obj'):
        model = cache.get('InMotionHostingmodel')
        parent_obj = cache.get('InMotionHostingparent_obj')
    else:
        model = InMotionHosting
        parent_obj = InMotionHostingParent
        cache.set('InMotionHostingmodel', model)
        cache.set('InMotionHostingparent_obj', parent_obj)
    like_obj = InMotionHostingLike

    def get_context_data(self, **kwargs):
        context = super(InMotionHostingDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = InMotionHostingComments.objects.filter(post=self.object)
        context['title'] = 'InMotionHosting'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(
                reverse_lazy('Hosting:inmotionhostingdetail', kwargs={'slug': self.kwargs['slug']}))

        else:
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


class A2HostingView(View):
    def get(self, request):
        slug = A2Hosting.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:a2hostingdetail', kwargs={'slug': slug}))


class A2HostingDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = A2HostingCommentsForm
    if cache.get('A2Hostingmodel') and cache.get('A2Hostingparent_obj'):
        model = cache.get('A2Hostingmodel')
        parent_obj = cache.get('A2Hostingparent_obj')
    else:
        model = A2Hosting
        parent_obj = A2HostingParent
        cache.set('A2Hostingmodel', model)
        cache.set('A2Hostingparent_obj', parent_obj)
    like_obj = A2HostingLike

    def get_context_data(self, **kwargs):
        context = super(A2HostingDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = A2HostingComments.objects.filter(post=self.object)
        context['title'] = 'A2Hosting'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:a2hostingdetail', kwargs={'slug': self.kwargs['slug']}))

        else:
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


class GreenGeeksView(View):
    def get(self, request):
        slug = GreenGeeks.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:greengeeksdetail', kwargs={'slug': slug}))


class GreenGeeksDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = GreenGeeksCommentsForm
    if cache.get('GreenGeeksmodel') and cache.get('GreenGeeksparent_obj'):
        model = cache.get('GreenGeeksmodel')
        parent_obj = cache.get('GreenGeeksparent_obj')
    else:
        model = GreenGeeks
        parent_obj = GreenGeeksParent
        cache.set('GreenGeeksmodel', model)
        cache.set('GreenGeeksparent_obj', parent_obj)
    like_obj = GreenGeeksLike

    def get_context_data(self, **kwargs):
        context = super(GreenGeeksDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = GreenGeeksComments.objects.filter(post=self.object)
        context['title'] = 'GreenGeeks'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:greengeeksdetail', kwargs={'slug': self.kwargs['slug']}))

        else:
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


class HostingerView(View):
    def get(self, request):
        slug = Hostinger.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:hostingerdetail', kwargs={'slug': slug}))


class HostingerDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = HostingerCommentsForm
    if cache.get('Hostingermodel') and cache.get('Hostingerparent_obj'):
        model = cache.get('Hostingermodel')
        parent_obj = cache.get('Hostingerparent_obj')
    else:
        model = Hostinger
        parent_obj = HostingerParent
        cache.set('Hostingermodel', model)
        cache.set('Hostingerparent_obj', parent_obj)
    like_obj = HostingerLike

    def get_context_data(self, **kwargs):
        context = super(HostingerDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = HostingerComments.objects.filter(post=self.object)
        context['title'] = 'Hostinger'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:hostingerdetail', kwargs={'slug': self.kwargs['slug']}))

        else:
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


class GoDaddyView(View):
    def get(self, request):
        slug = GoDaddy.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:godaddydetail', kwargs={'slug': slug}))


class GoDaddyDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = GoDaddyCommentsForm
    if cache.get('GoDaddymodel') and cache.get('GoDaddyparent_obj'):
        model = cache.get('GoDaddymodel')
        parent_obj = cache.get('GoDaddyparent_obj')
    else:
        model = GoDaddy
        parent_obj = GoDaddyParent
        cache.set('GoDaddymodel', model)
        cache.set('GoDaddyparent_obj', parent_obj)
    like_obj = GoDaddyLike

    def get_context_data(self, **kwargs):
        context = super(GoDaddyDetailView, self).get_context_data(**kwargs)
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
        context['comments'] = GoDaddyComments.objects.filter(post=self.object)
        context['title'] = 'GoDaddy'
        # View Counter
        s = self.object
        s.viewcounter += 1
        s.save()
        # Pagination
        next, prev = get_object_pagination(self.model, self.object)
        context['prev'] = prev
        context['next'] = next
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('type') == 'comment':
            form = self.form_class(request.POST)
            form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
            form.save()
            return HttpResponseRedirect(reverse_lazy('Hosting:godaddydetail', kwargs={'slug': self.kwargs['slug']}))
        else:
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
