from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, FormView, DetailView
from .models import *
from .forms import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy


# Create your views here.
class DBMSView(View):
    def get(self, request):
        slug = DBMS.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:dbmsdetail', kwargs={'slug': slug}))


class DBMSDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DBMSCommentsForm
    model = DBMS

    def get_context_data(self, **kwargs):
        context = super(DBMSDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DBMSComments.objects.filter(post=self.object)
        context['title'] = 'DBMS'
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
        return HttpResponseRedirect(reverse_lazy('Theory:dbmsdetail', kwargs={'slug': self.kwargs['slug']}))


class DataStructureView(View):
    def get(self, request):
        slug = DataStructure.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:datastructuredetail', kwargs={'slug': slug}))


class DataStructureDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DataStructureCommentsForm
    model = DataStructure

    def get_context_data(self, **kwargs):
        context = super(DataStructureDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DataStructureComments.objects.filter(post=self.object)
        context['title'] = 'Data Structure'
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
        return HttpResponseRedirect(reverse_lazy('Theory:datastructuredetail', kwargs={'slug': self.kwargs['slug']}))


class DAAView(View):
    def get(self, request):
        slug = DAA.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:daadetail', kwargs={'slug': slug}))


class DAADetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DAACommentsForm
    model = DAA

    def get_context_data(self, **kwargs):
        context = super(DAADetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DAAComments.objects.filter(post=self.object)
        context['title'] = 'DAA'
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
        return HttpResponseRedirect(reverse_lazy('Theory:daadetail', kwargs={'slug': self.kwargs['slug']}))


class OperatingSystemView(View):
    def get(self, request):
        slug = OperatingSystem.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:operatingsystemdetail', kwargs={'slug': slug}))


class OperatingSystemDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = OperatingSystemCommentsForm
    model = OperatingSystem

    def get_context_data(self, **kwargs):
        context = super(OperatingSystemDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = OperatingSystemComments.objects.filter(post=self.object)
        context['title'] = 'Operating System'
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
        return HttpResponseRedirect(reverse_lazy('Theory:operatingsystemdetail', kwargs={'slug': self.kwargs['slug']}))


class ComputeNetworkView(View):
    def get(self, request):
        slug = ComputerNetwork.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computernetworkdetail', kwargs={'slug': slug}))


class ComputerNetworkDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = ComputerNetworkCommentsForm
    model = ComputerNetwork

    def get_context_data(self, **kwargs):
        context = super(ComputerNetworkDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = ComputerNetworkComments.objects.filter(post=self.object)
        context['title'] = 'Computer Network'
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
        return HttpResponseRedirect(reverse_lazy('Theory:computernetworkdetail', kwargs={'slug': self.kwargs['slug']}))


class CompilerDesignView(View):
    def get(self, request):
        slug = CompilerDesign.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:compilerdesigndetail', kwargs={'slug': slug}))


class CompilerDesignDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = CompilerDesignCommentsForm
    model = CompilerDesign

    def get_context_data(self, **kwargs):
        context = super(CompilerDesignDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = CompilerDesignComments.objects.filter(post=self.object)
        context['title'] = 'Compiler Design'
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
        return HttpResponseRedirect(reverse_lazy('Theory:compilerdesigndetail', kwargs={'slug': self.kwargs['slug']}))


class ComputerOrganizationView(View):
    def get(self, request):
        slug = ComputerOrganization.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computerorganizationdetail', kwargs={'slug': slug}))


class ComputerOrganizationDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = ComputerOrganizationCommentsForm
    model = ComputerOrganization

    def get_context_data(self, **kwargs):
        context = super(ComputerOrganizationDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = ComputerOrganizationComments.objects.filter(post=self.object)
        context['title'] = 'Computer Organization'
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
        return HttpResponseRedirect(
            reverse_lazy('Theory:computerorganizationdetail', kwargs={'slug': self.kwargs['slug']}))


class DiscreteMathematicsView(View):
    def get(self, request):
        slug = DiscreteMathematics.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:discretemathematicsdetail', kwargs={'slug': slug}))


class DiscreteMathematicsDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DiscreteMathematicsCommentsForm
    model = DiscreteMathematics

    def get_context_data(self, **kwargs):
        context = super(DiscreteMathematicsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DiscreteMathematicsComments.objects.filter(post=self.object)
        context['title'] = 'Discrete Mathematics'
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
        return HttpResponseRedirect(
            reverse_lazy('Theory:discretemathematicsdetail', kwargs={'slug': self.kwargs['slug']}))


class SoftwareEngineeringView(View):
    def get(self, request):
        slug = SoftwareEngineering.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:softwareengineeringdetail', kwargs={'slug': slug}))


class SoftwareEngineeringDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = SoftwareEngineeringCommentsForm
    model = SoftwareEngineering

    def get_context_data(self, **kwargs):
        context = super(SoftwareEngineeringDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = SoftwareEngineeringComments.objects.filter(post=self.object)
        context['title'] = 'Software Engineering'
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
        return HttpResponseRedirect(
            reverse_lazy('Theory:softwareengineeringdetail', kwargs={'slug': self.kwargs['slug']}))


class CyberSecurityView(View):
    def get(self, request):
        slug = CyberSecurity.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:cybersecuritydetail', kwargs={'slug': slug}))


class CyberSecurityDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = CyberSecurityCommentsForm
    model = CyberSecurity

    def get_context_data(self, **kwargs):
        context = super(CyberSecurityDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = CyberSecurityComments.objects.filter(post=self.object)
        context['title'] = 'Cyber Security'
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
        return HttpResponseRedirect(reverse_lazy('Theory:cybersecuritydetail', kwargs={'slug': self.kwargs['slug']}))


class DataMiningView(View):
    def get(self, request):
        slug = DataMining.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:datamininganddatawarehousedetail', kwargs={'slug': slug}))


class DataMiningDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = DataMiningCommentsForm
    model = DataMining

    def get_context_data(self, **kwargs):
        context = super(DataMiningDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = DataMiningComments.objects.filter(post=self.object)
        context['title'] = 'Data Mining & Data Warehouse'
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
        return HttpResponseRedirect(
            reverse_lazy('Theory:datamininganddatawarehousedetail', kwargs={'slug': self.kwargs['slug']}))


class ArtificialIntelligenceView(View):
    def get(self, request):
        slug = ArtificialIntelligence.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:artificialintelligencedetail', kwargs={'slug': slug}))


class ArtificialIntelligenceDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = ArtificialIntelligenceCommentsForm
    model = ArtificialIntelligence

    def get_context_data(self, **kwargs):
        context = super(ArtificialIntelligenceDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = ArtificialIntelligenceComments.objects.filter(post=self.object)
        context['title'] = 'Artificial Intelligence'
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
        return HttpResponseRedirect(
            reverse_lazy('Theory:artificialintelligencedetail', kwargs={'slug': self.kwargs['slug']}))


class AutomataView(View):
    def get(self, request):
        slug = Automata.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:automatadetail', kwargs={'slug': slug}))


class AutomataDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = AutomataCommentsForm
    model = Automata

    def get_context_data(self, **kwargs):
        context = super(AutomataDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = AutomataComments.objects.filter(post=self.object)
        context['title'] = 'Automata'
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
        return HttpResponseRedirect(reverse_lazy('Theory:automatadetail', kwargs={'slug': self.kwargs['slug']}))


class ComputerGraphicsView(View):
    def get(self, request):
        slug = ComputerGraphics.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computergraphicsdetail', kwargs={'slug': slug}))


class ComputerGraphicsDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = ComputerGraphicsCommentsForm
    model = ComputerGraphics

    def get_context_data(self, **kwargs):
        context = super(ComputerGraphicsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = ComputerGraphicsComments.objects.filter(post=self.object)
        context['title'] = 'Computer Graphics'
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
        return HttpResponseRedirect(reverse_lazy('Theory:computergraphicsdetail', kwargs={'slug': self.kwargs['slug']}))


class WebApiView(View):
    def get(self, request):
        slug = WebApi.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:webapidetail', kwargs={'slug': slug}))


class WebAPIDetailView(DetailView, FormView):
    template_name = 'w3c/detail.html'
    form_class = WebApiCommentsForm
    model = WebApi

    def get_context_data(self, **kwargs):
        context = super(WebAPIDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = WebApiComments.objects.filter(post=self.object)
        context['title'] = 'Web API'
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
        return HttpResponseRedirect(reverse_lazy('Theory:webapidetail', kwargs={'slug': self.kwargs['slug']}))
