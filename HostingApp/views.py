from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, FormView, View
from .forms import *
from django.urls import reverse_lazy
from next_prev import next_in_order, prev_in_order
from django.contrib.auth.models import User
from django.http import JsonResponse


# Create your views here.
class DigitalOceanView(View):
    def get(self, request):
        slug = DigitalOcean.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Hosting:digitaloceandetail', kwargs={'slug': slug}))


class DigitalOceanDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DigitalOceanCommentsForm
    model = DigitalOcean
    like_obj = DigitalOceanLike
    parent_obj = DigitalOceanParent

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
    model = MSAzure
    like_obj = MSAzureLike
    parent_obj = MSAzureParent

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
    model = AWS
    like_obj = AWSLike
    parent_obj = AWSParent

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
    model = PythonAnywhere
    like_obj = PythonAnywhereLike
    parent_obj = PythonAnywhereParent

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
    model = HerokuApp
    like_obj = HerokuAppLike
    parent_obj = HerokuAppParent

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
    model = GithubHost
    like_obj = GithubHostLike
    parent_obj = GithubHostParent

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
    model = BlueHost
    like_obj = BlueHostLike
    parent_obj = BlueHostParent

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
    model = HostGator
    like_obj = HostGatorLike
    parent_obj = HostGatorParent

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
    model = InMotionHosting
    like_obj = InMotionHostingLike
    parent_obj = InMotionHostingParent

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
    model = A2Hosting
    like_obj = A2HostingLike
    parent_obj = A2HostingParent

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
    model = GreenGeeks
    like_obj = GreenGeeksLike
    parent_obj = GreenGeeksParent

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
    model = Hostinger
    like_obj = HostingerLike
    parent_obj = HostingerParent

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
    model = GoDaddy
    like_obj = GoDaddyLike
    parent_obj = GoDaddyParent

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
