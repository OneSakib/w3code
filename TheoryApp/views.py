from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import next_in_order, prev_in_order
from django.urls import reverse_lazy


# Create your views here.
class DBMSView(View):
    def get(self, request):
        slug = DBMS.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:dbmsdetail', kwargs={'slug': slug}))


class DBMSDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DBMS

    def get_context_data(self, **kwargs):
        context = super(DBMSDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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


class DataStructureView(View):
    def get(self, request):
        slug = DataStructure.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:datastructuredetail', kwargs={'slug': slug}))


class DataStructureDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DataStructure

    def get_context_data(self, **kwargs):
        context = super(DataStructureDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class DAAView(View):
    def get(self, request):
        slug = DAA.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:daadetail', kwargs={'slug': slug}))


class DAADetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DAA

    def get_context_data(self, **kwargs):
        context = super(DAADetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class OperatingSystemView(View):
    def get(self, request):
        slug = OperatingSystem.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:operatingsystemdetail', kwargs={'slug': slug}))


class OperatingSystemDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = OperatingSystem

    def get_context_data(self, **kwargs):
        context = super(OperatingSystemDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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


class ComputeNetworkView(View):
    def get(self, request):
        slug = ComputerNetwork.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computernetworkdetail', kwargs={'slug': slug}))


class ComputerNetworkDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = ComputerNetwork

    def get_context_data(self, **kwargs):
        context = super(ComputerNetworkDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class CompilerDesignView(View):
    def get(self, request):
        slug = CompilerDesign.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:compilerdesigndetail', kwargs={'slug': slug}))


class CompilerDesignDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = CompilerDesign

    def get_context_data(self, **kwargs):
        context = super(CompilerDesignDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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


class ComputerOrganizationView(View):
    def get(self, request):
        slug = ComputerOrganization.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computerorganizationdetail', kwargs={'slug': slug}))


class ComputerOrganizationDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = ComputerOrganization

    def get_context_data(self, **kwargs):
        context = super(ComputerOrganizationDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class DiscreteMathematicsView(View):
    def get(self, request):
        slug = DiscreteMathematics.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:discretemathematicsdetail', kwargs={'slug': slug}))


class DiscreteMathematicsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DiscreteMathematics

    def get_context_data(self, **kwargs):
        context = super(DiscreteMathematicsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class SoftwareEngineeringView(View):
    def get(self, request):
        slug = SoftwareEngineering.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:softwareengineeringdetail', kwargs={'slug': slug}))


class SoftwareEngineeringDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = SoftwareEngineering

    def get_context_data(self, **kwargs):
        context = super(SoftwareEngineeringDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class CyberSecurityView(View):
    def get(self, request):
        slug = CyberSecurity.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:cybersecuritydetail', kwargs={'slug': slug}))


class CyberSecurityDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = CyberSecurity

    def get_context_data(self, **kwargs):
        context = super(CyberSecurityDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class DataMiningView(View):
    def get(self, request):
        slug = DataMining.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:datamininganddatawarehousedetail', kwargs={'slug': slug}))


class DataMiningDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DataMining

    def get_context_data(self, **kwargs):
        context = super(DataMiningDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class ArtificialIntelligenceView(View):
    def get(self, request):
        slug = ArtificialIntelligence.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:artificialintelligencedetail', kwargs={'slug': slug}))


class ArtificialIntelligenceDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = ArtificialIntelligence

    def get_context_data(self, **kwargs):
        context = super(ArtificialIntelligenceDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class AutomataView(View):
    def get(self, request):
        slug = Automata.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:automatadetail', kwargs={'slug': slug}))


class AutomataDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Automata

    def get_context_data(self, **kwargs):
        context = super(AutomataDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class ComputerGraphicsView(View):
    def get(self, request):
        slug = ComputerGraphics.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computergraphicsdetail', kwargs={'slug': slug}))


class ComputerGraphicsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = ComputerGraphics

    def get_context_data(self, **kwargs):
        context = super(ComputerGraphicsDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class WebApiView(View):
    def get(self, request):
        slug = WebApi.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:webapidetail', kwargs={'slug': slug}))


class WebAPIDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = WebApi

    def get_context_data(self, **kwargs):
        context = super(WebAPIDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
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



class DDBMSView(View):
    def get(self, request):
        slug = DDBMS.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:ddbmsdetail', kwargs={'slug': slug}))


class DDBMSDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = DDBMS

    def get_context_data(self, **kwargs):
        context = super(DDBMSDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'DDBMS'
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
