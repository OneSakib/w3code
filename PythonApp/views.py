from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, FormView, DetailView
from .models import *
from .forms import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy


# Create your views here.
class DjangoView(View):
    def get(self, request):
        slug = Django.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:djangodetail', kwargs={'slug': slug}))


class DjangoDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DjangoCommentsForm
    model = Django

    def get_context_data(self, **kwargs):
        context = super(DjangoDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DjangoComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:djangodetail', kwargs={'slug': self.kwargs['slug']}))


class FlaskView(View):
    def get(self, request):
        slug = Flask.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:flaskdetail', kwargs={'slug': slug}))


class FlaskDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = FlaskCommentsForm
    model = Flask

    def get_context_data(self, **kwargs):
        context = super(FlaskDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = FlaskComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:flaskdetail', kwargs={'slug': self.kwargs['slug']}))


class MachineLearningView(View):
    def get(self, request):
        slug = MachineLearning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:machinelearningdetail', kwargs={'slug': slug}))


class MachineLearningDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = MachineLearningCommentsForm
    model = MachineLearning

    def get_context_data(self, **kwargs):
        context = super(MachineLearningDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = MachineLearningComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:machinelearningdetail', kwargs={'slug': self.kwargs['slug']}))


class NumpyView(View):
    def get(self, request):
        slug = Numpys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:numpydetail', kwargs={'slug': slug}))


class NumpyDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = NumpysCommentsForm
    model = Numpys

    def get_context_data(self, **kwargs):
        context = super(NumpyDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = NumpysComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:numpydetail', kwargs={'slug': self.kwargs['slug']}))


class TkinterView(View):
    def get(self, request):
        slug = Tkinters.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:tkinterdetail', kwargs={'slug': slug}))


class TkinterDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = TkintersCommentsForm
    model = Tkinters

    def get_context_data(self, **kwargs):
        context = super(TkinterDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = TkintersComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:tkinterdetail', kwargs={'slug': self.kwargs['slug']}))


class PytorchView(View):
    def get(self, request):
        slug = Pytorchs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pytorchdetail', kwargs={'slug': slug}))


class PytorchDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = PytorchsCommentsForm
    model = Pytorchs

    def get_context_data(self, **kwargs):
        context = super(PytorchDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = PytorchsComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:pytorchdetail', kwargs={'slug': self.kwargs['slug']}))


class PygameView(View):
    def get(self, request):
        slug = Pygames.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pygamedetail', kwargs={'slug': slug}))


class PygameDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = PygamesCommentsForm
    model = Pygames

    def get_context_data(self, **kwargs):
        context = super(PygameDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = PygamesComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:pygamedetail', kwargs={'slug': self.kwargs['slug']}))


class ScipyView(View):
    def get(self, request):
        slug = Scipys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:scipydetail', kwargs={'slug': slug}))


class ScipyDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = ScipysCommentsForm
    model = Scipys

    def get_context_data(self, **kwargs):
        context = super(ScipyDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = ScipysComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:scipydetail', kwargs={'slug': self.kwargs['slug']}))


class PandasView(View):
    def get(self, request):
        slug = Pandass.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pandasdetail', kwargs={'slug': slug}))


class PandasDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = PandassCommentsForm
    model = Pandass

    def get_context_data(self, **kwargs):
        context = super(PandasDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = PandassComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:pandasdetail', kwargs={'slug': self.kwargs['slug']}))


class OpenCVView(View):
    def get(self, request):
        slug = OpenCVs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:opencvdetail', kwargs={'slug': slug}))


class OpenCVDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = OpenCVsCommentsForm
    model = OpenCVs

    def get_context_data(self, **kwargs):
        context = super(OpenCVDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = OpenCVsComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:opencvdetail', kwargs={'slug': self.kwargs['slug']}))


class MatplotlibView(View):
    def get(self, request):
        slug = Matplotlibs.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:matplotlibdetail', kwargs={'slug': slug}))


class MatplotlibDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = MatplotlibsCommentsForm
    model = Matplotlibs

    def get_context_data(self, **kwargs):
        context = super(MatplotlibDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = MatplotlibsComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:matplotlibdetail', kwargs={'slug': self.kwargs['slug']}))


class SeleniumView(View):
    def get(self, request):
        slug = Seleniums.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:seleniumdetail', kwargs={'slug': slug}))


class SeleniumDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = SeleniumsCommentsForm
    model = Seleniums

    def get_context_data(self, **kwargs):
        context = super(SeleniumDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = SeleniumsComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:seleniumdetail', kwargs={'slug': self.kwargs['slug']}))


class KivyView(View):
    def get(self, request):
        slug = Kivys.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:kivydetail', kwargs={'slug': slug}))


class KivyDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = KivysCommentsForm
    model = Kivys

    def get_context_data(self, **kwargs):
        context = super(KivyDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = KivysComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:kivydetail', kwargs={'slug': self.kwargs['slug']}))


class JupyterView(View):
    def get(self, request):
        slug = Jupyters.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:jupyterdetail', kwargs={'slug': slug}))


class JupyterDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = JupytersCommentsForm
    model = Jupyters

    def get_context_data(self, **kwargs):
        context = super(JupyterDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = JupytersComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:jupyterdetail', kwargs={'slug': self.kwargs['slug']}))


class DataScienceView(View):
    def get(self, request):
        slug = DataScience.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:datasciencedetail', kwargs={'slug': slug}))


class DataScienceDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DataScienceCommentsForm
    model = DataScience

    def get_context_data(self, **kwargs):
        context = super(DataScienceDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DataScienceComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:datasciencedetail', kwargs={'slug': self.kwargs['slug']}))


class DeepLearningView(View):
    def get(self, request):
        slug = DeepLearning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:deeplearningdetail', kwargs={'slug': slug}))


class DeepLearningDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DeepLearningCommentsForm
    model = DeepLearning

    def get_context_data(self, **kwargs):
        context = super(DeepLearningDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DeepLearningComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:deeplearningdetail', kwargs={'slug': self.kwargs['slug']}))


class PillowView(View):
    def get(self, request):
        slug = Pillows.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:pillowdetail', kwargs={'slug': slug}))


class PillowDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = PillowsCommentsForm
    model = Pillows

    def get_context_data(self, **kwargs):
        context = super(PillowDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = PillowsComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:pillowdetail', kwargs={'slug': self.kwargs['slug']}))


class TensorflowView(View):
    def get(self, request):
        slug = Tensorflows.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Python:tensorflowdetail', kwargs={'slug': slug}))


class TensorFlowDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = TensorflowsCommentsForm
    model = Tensorflows

    def get_context_data(self, **kwargs):
        context = super(TensorFlowDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = TensorflowsComments.objects.filter(post=self.object)
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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.post = self.model.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('Python:tensorflowdetail', kwargs={'slug': self.kwargs['slug']}))
