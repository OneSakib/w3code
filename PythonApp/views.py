from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *


# Create your views here.
class DjangoView(View):
    def get(self, request):
        slug = Django.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:djangodetail', kwargs={'slug': slug}))


class DjangoDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Djangomodel') and cache.get('Djangoparent_obj'):
        model = cache.get('Djangomodel')
        parent_obj = cache.get('Djangoparent_obj')
    else:
        model = Django
        parent_obj = DjangoParent
        cache.set('Djangomodel', model)
        cache.set('Djangoparent_obj', parent_obj)
    like_obj = DjangoLike

    def get_context_data(self, **kwargs):
        context = super(DjangoDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Django'
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


class RestApiView(View):
    def get(self, request):
        slug = RestApi.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:restapidetail', kwargs={'slug': slug}))


class RestApiDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('RestApimodel') and cache.get('RestApiparent_obj'):
        model = cache.get('RestApimodel')
        parent_obj = cache.get('RestApiparent_obj')
    else:
        model = RestApi
        parent_obj = RestApiParent
        cache.set('RestApimodel', model)
        cache.set('RestApiparent_obj', parent_obj)
    like_obj = RestApiLike

    def get_context_data(self, **kwargs):
        context = super(RestApiDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'RestApi'
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


class FlaskView(View):
    def get(self, request):
        slug = Flask.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:flaskdetail', kwargs={'slug': slug}))


class FlaskDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Flaskmodel') and cache.get('Flaskparent_obj'):
        model = cache.get('Flaskmodel')
        parent_obj = cache.get('Flaskparent_obj')
    else:
        model = Flask
        parent_obj = FlaskParent
        cache.set('Flaskmodel', model)
        cache.set('Flaskparent_obj', parent_obj)
    like_obj = FlaskLike

    def get_context_data(self, **kwargs):
        context = super(FlaskDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Flask'
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


class MachineLearningView(View):
    def get(self, request):
        slug = MachineLearning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:machinelearningdetail', kwargs={'slug': slug}))


class MachineLearningDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('MachineLearningmodel') and cache.get('MachineLearningparent_obj'):
        model = cache.get('MachineLearningmodel')
        parent_obj = cache.get('MachineLearningparent_obj')
    else:
        model = MachineLearning
        parent_obj = MachineLearningParent
        cache.set('MachineLearningmodel', model)
        cache.set('MachineLearningparent_obj', parent_obj)
    like_obj = MachineLearningLike

    def get_context_data(self, **kwargs):
        context = super(MachineLearningDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Machine Learning'
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


class NumpyView(View):
    def get(self, request):
        slug = Numpys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:numpydetail', kwargs={'slug': slug}))


class NumpyDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Numpysmodel') and cache.get('Numpysparent_obj'):
        model = cache.get('Numpysmodel')
        parent_obj = cache.get('Numpysparent_obj')
    else:
        model = Numpys
        parent_obj = NumpysParent
        cache.set('Numpysmodel', model)
        cache.set('Numpysparent_obj', parent_obj)
    like_obj = NumpysLike

    def get_context_data(self, **kwargs):
        context = super(NumpyDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Numpy'
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


class TkinterView(View):
    def get(self, request):
        slug = Tkinters.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:tkinterdetail', kwargs={'slug': slug}))


class TkinterDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('TkintersLikemodel') and cache.get('TkintersLikeparent_obj'):
        model = cache.get('TkintersLikemodel')
        parent_obj = cache.get('TkintersLikeparent_obj')
    else:
        model = Tkinters
        parent_obj = TkintersParent
        cache.set('TkintersLikemodel', model)
        cache.set('TkintersLikeparent_obj', parent_obj)
    like_obj = TkintersLike

    def get_context_data(self, **kwargs):
        context = super(TkinterDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Tkinter'
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


class PytorchView(View):
    def get(self, request):
        slug = Pytorchs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pytorchdetail', kwargs={'slug': slug}))


class PytorchDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Pytorchsmodel') and cache.get('Pytorchsparent_obj'):
        model = cache.get('Pytorchsmodel')
        parent_obj = cache.get('Pytorchsparent_obj')
    else:
        model = Pytorchs
        parent_obj = PytorchsParent
        cache.set('Pytorchsmodel', model)
        cache.set('Pytorchsparent_obj', parent_obj)
    like_obj = PytorchsLike

    def get_context_data(self, **kwargs):
        context = super(PytorchDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Pytorch'
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


class PygameView(View):
    def get(self, request):
        slug = Pygames.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pygamedetail', kwargs={'slug': slug}))


class PygameDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Pygamesmodel') and cache.get('Pygamesparent_obj'):
        model = cache.get('Pygamesmodel')
        parent_obj = cache.get('Pygamesparent_obj')
    else:
        model = Pygames
        parent_obj = PygamesParent
        cache.set('Pygamesmodel', model)
        cache.set('Pygamesparent_obj', parent_obj)
    like_obj = PygamesLike

    def get_context_data(self, **kwargs):
        context = super(PygameDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'PyGame'
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


class ScipyView(View):
    def get(self, request):
        slug = Scipys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:scipydetail', kwargs={'slug': slug}))


class ScipyDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Scipysmodel') and cache.get('Scipysparent_obj'):
        model = cache.get('Scipysmodel')
        parent_obj = cache.get('Scipysparent_obj')
    else:
        model = Scipys
        parent_obj = ScipysParent
        cache.set('Scipysmodel', model)
        cache.set('Scipysparent_obj', parent_obj)
    like_obj = ScipysLike

    def get_context_data(self, **kwargs):
        context = super(ScipyDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'SciPy'
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


class PandasView(View):
    def get(self, request):
        slug = Pandass.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pandasdetail', kwargs={'slug': slug}))


class PandasDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Pandassmodel') and cache.get('Pandassparent_obj'):
        model = cache.get('Pandassmodel')
        parent_obj = cache.get('Pandassparent_obj')
    else:
        model = Pandass
        parent_obj = PandassParent
        cache.set('Pandassmodel', model)
        cache.set('Pandassparent_obj', parent_obj)
    like_obj = PandassLike

    def get_context_data(self, **kwargs):
        context = super(PandasDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Pandas'
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


class OpenCVView(View):
    def get(self, request):
        slug = OpenCVs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:opencvdetail', kwargs={'slug': slug}))


class OpenCVDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('OpenCVsmodel') and cache.get('OpenCVsparent_obj'):
        model = cache.get('OpenCVsmodel')
        parent_obj = cache.get('OpenCVsparent_obj')
    else:
        model = OpenCVs
        parent_obj = OpenCVsParent
        cache.set('OpenCVsmodel', model)
        cache.set('OpenCVsparent_obj', parent_obj)
    like_obj = OpenCVsLike

    def get_context_data(self, **kwargs):
        context = super(OpenCVDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'OpenCV'
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


class MatplotlibView(View):
    def get(self, request):
        slug = Matplotlibs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:matplotlibdetail', kwargs={'slug': slug}))


class MatplotlibDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Matplotlibsmodel') and cache.get('Matplotlibsparent_obj'):
        model = cache.get('Matplotlibsmodel')
        parent_obj = cache.get('Matplotlibsparent_obj')
    else:
        model = Matplotlibs
        parent_obj = MatplotlibsParent
        cache.set('Matplotlibsmodel', model)
        cache.set('Matplotlibsparent_obj', parent_obj)
    like_obj = MatplotlibsLike

    def get_context_data(self, **kwargs):
        context = super(MatplotlibDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Matplotlib'
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


class SeleniumView(View):
    def get(self, request):
        slug = Seleniums.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:seleniumdetail', kwargs={'slug': slug}))


class SeleniumDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Seleniumsmodel') and cache.get('Seleniumsparent_obj'):
        model = cache.get('Seleniumsmodel')
        parent_obj = cache.get('Seleniumsparent_obj')
    else:
        model = Seleniums
        parent_obj = SeleniumsParent
        cache.set('Seleniumsmodel', model)
        cache.set('Seleniumsparent_obj', parent_obj)
    like_obj = SeleniumsLike

    def get_context_data(self, **kwargs):
        context = super(SeleniumDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Selenium'
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


class KivyView(View):
    def get(self, request):
        slug = Kivys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:kivydetail', kwargs={'slug': slug}))


class KivyDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Kivysmodel') and cache.get('Kivysparent_obj'):
        model = cache.get('Kivysmodel')
        parent_obj = cache.get('Kivysparent_obj')
    else:
        model = Kivys
        parent_obj = KivysParent
        cache.set('Kivysmodel', model)
        cache.set('Kivysparent_obj', parent_obj)
    like_obj = KivysLike

    def get_context_data(self, **kwargs):
        context = super(KivyDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Kivy'
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


class JupyterView(View):
    def get(self, request):
        slug = Jupyters.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:jupyterdetail', kwargs={'slug': slug}))


class JupyterDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Jupytersmodel') and cache.get('Jupytersparent_obj'):
        model = cache.get('Jupytersmodel')
        parent_obj = cache.get('Jupytersparent_obj')
    else:
        model = Jupyters
        parent_obj = JupytersParent
        cache.set('Jupytersmodel', model)
        cache.set('Jupytersparent_obj', parent_obj)
    like_obj = JupytersLike

    def get_context_data(self, **kwargs):
        context = super(JupyterDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Jupyter'
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


class DataScienceView(View):
    def get(self, request):
        slug = DataScience.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:datasciencedetail', kwargs={'slug': slug}))


class DataScienceDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DataSciencemodel') and cache.get('DataScienceparent_obj'):
        model = cache.get('DataSciencemodel')
        parent_obj = cache.get('DataScienceparent_obj')
    else:
        model = DataScience
        parent_obj = DataScienceParent
        cache.set('DataSciencemodel', model)
        cache.set('DataScienceparent_obj', parent_obj)
    like_obj = DataScienceLike

    def get_context_data(self, **kwargs):
        context = super(DataScienceDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Data Science'
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


class DeepLearningView(View):
    def get(self, request):
        slug = DeepLearning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:deeplearningdetail', kwargs={'slug': slug}))


class DeepLearningDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DeepLearningmodel') and cache.get('DeepLearningparent_obj'):
        model = cache.get('DeepLearningmodel')
        parent_obj = cache.get('DeepLearningparent_obj')
    else:
        model = DeepLearning
        parent_obj = DeepLearningParent
        cache.set('DeepLearningmodel', model)
        cache.set('DeepLearningparent_obj', parent_obj)
    like_obj = DeepLearningLike

    def get_context_data(self, **kwargs):
        context = super(DeepLearningDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Deep Learning'
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


class PillowView(View):
    def get(self, request):
        slug = Pillows.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pillowdetail', kwargs={'slug': slug}))


class PillowDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Pillowsmodel') and cache.get('Pillowsparent_obj'):
        model = cache.get('Pillowsmodel')
        parent_obj = cache.get('Pillowsparent_obj')
    else:
        model = Pillows
        parent_obj = PillowsParent
        cache.set('Pillowsmodel', model)
        cache.set('Pillowsparent_obj', parent_obj)
    like_obj = PillowsLike

    def get_context_data(self, **kwargs):
        context = super(PillowDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Pillow'
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


class TensorflowView(View):
    def get(self, request):
        slug = Tensorflows.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:tensorflowdetail', kwargs={'slug': slug}))


class TensorFlowDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Tensorflowsmodel') and cache.get('Tensorflowsparent_obj'):
        model = cache.get('Tensorflowsmodel')
        parent_obj = cache.get('Tensorflowsparent_obj')
    else:
        model = Tensorflows
        parent_obj = TensorflowsParent
        cache.set('Tensorflowsmodel', model)
        cache.set('Tensorflowsparent_obj', parent_obj)
    like_obj = TensorflowsLike

    def get_context_data(self, **kwargs):
        context = super(TensorFlowDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Tensorflow'
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


class DSPythonView(View):
    def get(self, request):
        slug = DSPython.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:dspythondetail', kwargs={'slug': slug}))


class DSPythonDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DSPythonmodel') and cache.get('DSPythonparent_obj'):
        model = cache.get('DSPythonmodel')
        parent_obj = cache.get('DSPythonparent_obj')
    else:
        model = DSPython
        parent_obj = DSPythonParent
        cache.set('DSPythonmodel', model)
        cache.set('DSPythonparent_obj', parent_obj)
    like_obj = DSPythonLike

    def get_context_data(self, **kwargs):
        context = super(DSPythonDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'DSPython'
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
