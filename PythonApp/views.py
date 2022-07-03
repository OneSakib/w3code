from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy


# Create your views here.
class DjangoView(View):
    def get(self, request):
        slug = Django.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:djangodetail', kwargs={'slug': slug}))


class DjangoDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Django

    def get_context_data(self, **kwargs):
        context = super(DjangoDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Django'
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


class RestApiView(View):
    def get(self, request):
        slug = RestApi.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:restapidetail', kwargs={'slug': slug}))


class RestApiDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = RestApi

    def get_context_data(self, **kwargs):
        context = super(RestApiDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'RestApi'
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


class FlaskView(View):
    def get(self, request):
        slug = Flask.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:flaskdetail', kwargs={'slug': slug}))


class FlaskDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Flask

    def get_context_data(self, **kwargs):
        context = super(FlaskDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Flask'
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


class MachineLearningView(View):
    def get(self, request):
        slug = MachineLearning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:machinelearningdetail', kwargs={'slug': slug}))


class MachineLearningDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = MachineLearning

    def get_context_data(self, **kwargs):
        context = super(MachineLearningDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Machine Learning'
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


class NumpyView(View):
    def get(self, request):
        slug = Numpys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:numpydetail', kwargs={'slug': slug}))


class NumpyDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Numpys

    def get_context_data(self, **kwargs):
        context = super(NumpyDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Numpy'
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


class TkinterView(View):
    def get(self, request):
        slug = Tkinters.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:tkinterdetail', kwargs={'slug': slug}))


class TkinterDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Tkinters

    def get_context_data(self, **kwargs):
        context = super(TkinterDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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


class PytorchView(View):
    def get(self, request):
        slug = Pytorchs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pytorchdetail', kwargs={'slug': slug}))


class PytorchDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Pytorchs

    def get_context_data(self, **kwargs):
        context = super(PytorchDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Pytorch'
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


class PygameView(View):
    def get(self, request):
        slug = Pygames.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pygamedetail', kwargs={'slug': slug}))


class PygameDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Pygames

    def get_context_data(self, **kwargs):
        context = super(PygameDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'PyGame'
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


class ScipyView(View):
    def get(self, request):
        slug = Scipys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:scipydetail', kwargs={'slug': slug}))


class ScipyDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Scipys

    def get_context_data(self, **kwargs):
        context = super(ScipyDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'SciPy'
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


class PandasView(View):
    def get(self, request):
        slug = Pandass.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pandasdetail', kwargs={'slug': slug}))


class PandasDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Pandass

    def get_context_data(self, **kwargs):
        context = super(PandasDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Pandas'
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


class OpenCVView(View):
    def get(self, request):
        slug = OpenCVs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:opencvdetail', kwargs={'slug': slug}))


class OpenCVDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = OpenCVs

    def get_context_data(self, **kwargs):
        context = super(OpenCVDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'OpenCV'
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


class MatplotlibView(View):
    def get(self, request):
        slug = Matplotlibs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:matplotlibdetail', kwargs={'slug': slug}))


class MatplotlibDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Matplotlibs

    def get_context_data(self, **kwargs):
        context = super(MatplotlibDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Matplotlib'
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


class SeleniumView(View):
    def get(self, request):
        slug = Seleniums.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:seleniumdetail', kwargs={'slug': slug}))


class SeleniumDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Seleniums

    def get_context_data(self, **kwargs):
        context = super(SeleniumDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Selenium'
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


class KivyView(View):
    def get(self, request):
        slug = Kivys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:kivydetail', kwargs={'slug': slug}))


class KivyDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Kivys

    def get_context_data(self, **kwargs):
        context = super(KivyDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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


class JupyterView(View):
    def get(self, request):
        slug = Jupyters.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:jupyterdetail', kwargs={'slug': slug}))


class JupyterDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Jupyters

    def get_context_data(self, **kwargs):
        context = super(JupyterDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Jupyter'
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


class DataScienceView(View):
    def get(self, request):
        slug = DataScience.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:datasciencedetail', kwargs={'slug': slug}))


class DataScienceDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DataScience

    def get_context_data(self, **kwargs):
        context = super(DataScienceDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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


class DeepLearningView(View):
    def get(self, request):
        slug = DeepLearning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:deeplearningdetail', kwargs={'slug': slug}))


class DeepLearningDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DeepLearning

    def get_context_data(self, **kwargs):
        context = super(DeepLearningDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Deep Learning'
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


class PillowView(View):
    def get(self, request):
        slug = Pillows.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pillowdetail', kwargs={'slug': slug}))


class PillowDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Pillows

    def get_context_data(self, **kwargs):
        context = super(PillowDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Pillow'
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


class TensorflowView(View):
    def get(self, request):
        slug = Tensorflows.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:tensorflowdetail', kwargs={'slug': slug}))


class TensorFlowDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Tensorflows

    def get_context_data(self, **kwargs):
        context = super(TensorFlowDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Tensorflow'
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


class DSPythonView(View):
    def get(self, request):
        slug = DSPython.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:dspythondetail', kwargs={'slug': slug}))


class DSPythonDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DSPython

    def get_context_data(self, **kwargs):
        context = super(DSPythonDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'DSPython'
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
