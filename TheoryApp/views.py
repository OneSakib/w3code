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
class DBMSView(View):
    def get(self, request):
        slug = DBMS.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:dbmsdetail', kwargs={'slug': slug}))


class DBMSDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DBMSmodel') and cache.get('DBMSparent_obj'):
        model = cache.get('DBMSmodel')
        parent_obj = cache.get('DBMSparent_obj')
    else:
        model = DBMS
        parent_obj = DBMSParent
        cache.set('DBMSmodel', model)
        cache.set('DBMSparent_obj', parent_obj)
    like_obj = DBMSLike

    def get_context_data(self, **kwargs):
        context = super(DBMSDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'DBMS'
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


class DataStructureView(View):
    def get(self, request):
        slug = DataStructure.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:datastructuredetail', kwargs={'slug': slug}))


class DataStructureDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DataStructuremodel') and cache.get('DataStructureparent_obj'):
        model = cache.get('DataStructuremodel')
        parent_obj = cache.get('DataStructureparent_obj')
    else:
        model = DataStructure
        parent_obj = DataStructureParent
        cache.set('DataStructuremodel', model)
        cache.set('DataStructureparent_obj', parent_obj)
    like_obj = DataStructureLike

    def get_context_data(self, **kwargs):
        context = super(DataStructureDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Data Structure'
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


class DAAView(View):
    def get(self, request):
        slug = DAA.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:daadetail', kwargs={'slug': slug}))


class DAADetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DAAmodel') and cache.get('DAAparent_obj'):
        model = cache.get('DAAmodel')
        parent_obj = cache.get('DAAparent_obj')
    else:
        model = DAA
        parent_obj = DAAParent
        cache.set('DAAmodel', model)
        cache.set('DAAparent_obj', parent_obj)
    like_obj = DAALike

    def get_context_data(self, **kwargs):
        context = super(DAADetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'DAA'
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


class OperatingSystemView(View):
    def get(self, request):
        slug = OperatingSystem.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:operatingsystemdetail', kwargs={'slug': slug}))


class OperatingSystemDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('OperatingSystemmodel') and cache.get('OperatingSystemparent_obj'):
        model = cache.get('OperatingSystemmodel')
        parent_obj = cache.get('OperatingSystemparent_obj')
    else:
        model = OperatingSystem
        parent_obj = OperatingSystemParent
        cache.set('OperatingSystemmodel', model)
        cache.set('OperatingSystemparent_obj', parent_obj)
    like_obj = OperatingSystemLike

    def get_context_data(self, **kwargs):
        context = super(OperatingSystemDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Operating System'
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


class ComputeNetworkView(View):
    def get(self, request):
        slug = ComputerNetwork.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computernetworkdetail', kwargs={'slug': slug}))


class ComputerNetworkDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('ComputerNetworkmodel') and cache.get('ComputerNetworkparent_obj'):
        model = cache.get('ComputerNetworkmodel')
        parent_obj = cache.get('ComputerNetworkparent_obj')
    else:
        model = ComputerNetwork
        parent_obj = ComputerNetworkParent
        cache.set('ComputerNetworkmodel', model)
        cache.set('ComputerNetworkparent_obj', parent_obj)
    like_obj = ComputerNetworkLike

    def get_context_data(self, **kwargs):
        context = super(ComputerNetworkDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Computer Network'
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


class CompilerDesignView(View):
    def get(self, request):
        slug = CompilerDesign.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:compilerdesigndetail', kwargs={'slug': slug}))


class CompilerDesignDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('CompilerDesignmodel') and cache.get('CompilerDesignparent_obj'):
        model = cache.get('CompilerDesignmodel')
        parent_obj = cache.get('CompilerDesignparent_obj')
    else:
        model = CompilerDesign
        parent_obj = CompilerDesignParent
        cache.set('CompilerDesignmodel', model)
        cache.set('CompilerDesignparent_obj', parent_obj)
    like_obj = CompilerDesignLike

    def get_context_data(self, **kwargs):
        context = super(CompilerDesignDetailView, self).get_context_data(**kwargs)
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


class ComputerOrganizationView(View):
    def get(self, request):
        slug = ComputerOrganization.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computerorganizationdetail', kwargs={'slug': slug}))


class ComputerOrganizationDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('ComputerOrganizationmodel') and cache.get('ComputerOrganizationparent_obj'):
        model = cache.get('ComputerOrganizationmodel')
        parent_obj = cache.get('ComputerOrganizationparent_obj')
    else:
        model = ComputerOrganization
        parent_obj = ComputerOrganizationParent
        cache.set('ComputerOrganizationmodel', model)
        cache.set('ComputerOrganizationparent_obj', parent_obj)
    like_obj = ComputerOrganizationLike

    def get_context_data(self, **kwargs):
        context = super(ComputerOrganizationDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Computer Organization'
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


class DiscreteMathematicsView(View):
    def get(self, request):
        slug = DiscreteMathematics.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:discretemathematicsdetail', kwargs={'slug': slug}))


class DiscreteMathematicsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DiscreteMathematicsmodel') and cache.get('DiscreteMathematicsparent_obj'):
        model = cache.get('DiscreteMathematicsmodel')
        parent_obj = cache.get('DiscreteMathematicsparent_obj')
    else:
        model = DiscreteMathematics
        parent_obj = DiscreteMathematicsParent
        cache.set('DiscreteMathematicsmodel', model)
        cache.set('DiscreteMathematicsparent_obj', parent_obj)
    like_obj = DiscreteMathematicsLike

    def get_context_data(self, **kwargs):
        context = super(DiscreteMathematicsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Discrete Mathematics'
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


class SoftwareEngineeringView(View):
    def get(self, request):
        slug = SoftwareEngineering.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:softwareengineeringdetail', kwargs={'slug': slug}))


class SoftwareEngineeringDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('SoftwareEngineeringmodel') and cache.get('SoftwareEngineeringparent_obj'):
        model = cache.get('SoftwareEngineeringmodel')
        parent_obj = cache.get('SoftwareEngineeringparent_obj')
    else:
        model = SoftwareEngineering
        parent_obj = SoftwareEngineeringParent
        cache.set('SoftwareEngineeringmodel', model)
        cache.set('SoftwareEngineeringparent_obj', parent_obj)
    like_obj = SoftwareEngineeringLike

    def get_context_data(self, **kwargs):
        context = super(SoftwareEngineeringDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Software Engineering'
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


class CyberSecurityView(View):
    def get(self, request):
        slug = CyberSecurity.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:cybersecuritydetail', kwargs={'slug': slug}))


class CyberSecurityDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('CyberSecuritymodel') and cache.get('CyberSecurityparent_obj'):
        model = cache.get('CyberSecuritymodel')
        parent_obj = cache.get('CyberSecurityparent_obj')
    else:
        model = CyberSecurity
        parent_obj = CyberSecurityParent
        cache.set('CyberSecuritymodel', model)
        cache.set('CyberSecurityparent_obj', parent_obj)
    like_obj = CyberSecurityLike

    def get_context_data(self, **kwargs):
        context = super(CyberSecurityDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Cyber Security'
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


class DataMiningView(View):
    def get(self, request):
        slug = DataMining.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:datamininganddatawarehousedetail', kwargs={'slug': slug}))


class DataMiningDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DataMiningmodel') and cache.get('DataMiningparent_obj'):
        model = cache.get('DataMiningmodel')
        parent_obj = cache.get('DataMiningparent_obj')
    else:
        model = DataMining
        parent_obj = DataMiningParent
        cache.set('DataMiningmodel', model)
        cache.set('DataMiningparent_obj', parent_obj)
    like_obj = DataMiningLike

    def get_context_data(self, **kwargs):
        context = super(DataMiningDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Data Mining & Data Warehouse'
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


class ArtificialIntelligenceView(View):
    def get(self, request):
        slug = ArtificialIntelligence.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:artificialintelligencedetail', kwargs={'slug': slug}))


class ArtificialIntelligenceDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('ArtificialIntelligencemodel') and cache.get('ArtificialIntelligenceparent_obj'):
        model = cache.get('ArtificialIntelligencemodel')
        parent_obj = cache.get('ArtificialIntelligenceparent_obj')
    else:
        model = ArtificialIntelligence
        parent_obj = ArtificialIntelligenceParent
        cache.set('ArtificialIntelligencemodel', model)
        cache.set('ArtificialIntelligenceparent_obj', parent_obj)
    like_obj = ArtificialIntelligenceLike

    def get_context_data(self, **kwargs):
        context = super(ArtificialIntelligenceDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Artificial Intelligence'
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


class AutomataView(View):
    def get(self, request):
        slug = Automata.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:automatadetail', kwargs={'slug': slug}))


class AutomataDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Automatamodel') and cache.get('Automataparent_obj'):
        model = cache.get('Automatamodel')
        parent_obj = cache.get('Automataparent_obj')
    else:
        model = Automata
        parent_obj = AutomataParent
        cache.set('Automatamodel', model)
        cache.set('Automataparent_obj', parent_obj)
    like_obj = AutomataLike

    def get_context_data(self, **kwargs):
        context = super(AutomataDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Automata'
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


class ComputerGraphicsView(View):
    def get(self, request):
        slug = ComputerGraphics.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:computergraphicsdetail', kwargs={'slug': slug}))


class ComputerGraphicsDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('ComputerGraphicsmodel') and cache.get('ComputerGraphicsparent_obj'):
        model = cache.get('ComputerGraphicsmodel')
        parent_obj = cache.get('ComputerGraphicsparent_obj')
    else:
        model = ComputerGraphics
        parent_obj = ComputerGraphicsParent
        cache.set('ComputerGraphicsmodel', model)
        cache.set('ComputerGraphicsparent_obj', parent_obj)
    like_obj = ComputerGraphicsLike

    def get_context_data(self, **kwargs):
        context = super(ComputerGraphicsDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Computer Graphics'
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


class WebApiView(View):
    def get(self, request):
        slug = WebApi.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:webapidetail', kwargs={'slug': slug}))


class WebAPIDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('WebApimodel') and cache.get('WebApiparent_obj'):
        model = cache.get('WebApimodel')
        parent_obj = cache.get('WebApiparent_obj')
    else:
        model = WebApi
        parent_obj = WebApiParent
        cache.set('WebApimodel', model)
        cache.set('WebApiparent_obj', parent_obj)
    like_obj = WebApiLike

    def get_context_data(self, **kwargs):
        context = super(WebAPIDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Web API'
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


class DDBMSView(View):
    def get(self, request):
        slug = DDBMS.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Theory:ddbmsdetail', kwargs={'slug': slug}))


class DDBMSDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('DDBMSmodel') and cache.get('DDBMSparent_obj'):
        model = cache.get('DDBMSmodel')
        parent_obj = cache.get('DDBMSparent_obj')
    else:
        model = DDBMS
        parent_obj = DDBMSParent
        cache.set('DDBMSmodel', model)
        cache.set('DDBMSparent_obj', parent_obj)
    like_obj = DDBMSLike

    def get_context_data(self, **kwargs):
        context = super(DDBMSDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'DDBMS'
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
