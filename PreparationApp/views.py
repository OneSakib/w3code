from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import next_in_order, prev_in_order
from django.contrib.auth.models import User
from django.http import JsonResponse
from MainApp.views import CACHE_TTL, cache
from MainApp.functions import *


# Create your views here.
class AptitudeView(View):
    def get(self, request):
        slug = Aptitude.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:aptitudedetail', kwargs={'slug': slug}))


class AptitudeDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Aptitudemodel') and cache.get('Aptitudeparent_obj'):
        model = cache.get('Aptitudemodel')
        parent_obj = cache.get('Aptitudeparent_obj')
    else:
        model = Aptitude
        parent_obj = AptitudeParent
        cache.set('Aptitudemodel', model)
        cache.set('Aptitudeparent_obj', parent_obj)
    like_obj = AptitudeLike

    def get_context_data(self, **kwargs):
        context = super(AptitudeDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Aptitude'
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


class ReasoningView(View):
    def get(self, request):
        slug = Reasoning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:reasoningdetail', kwargs={'slug': slug}))


class ReasoningDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('Reasoningmodel') and cache.get('Reasoningparent_obj'):
        model = cache.get('Reasoningmodel')
        parent_obj = cache.get('Reasoningparent_obj')
    else:
        model = Reasoning
        parent_obj = ReasoningParent
        cache.set('Reasoningmodel', model)
        cache.set('Reasoningparent_obj', parent_obj)
    like_obj = ReasoningLike

    def get_context_data(self, **kwargs):
        context = super(ReasoningDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Reasoning'
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


class VerbalAbilityView(View):
    def get(self, request):
        slug = VerbalAbility.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:verbalabilitydetail', kwargs={'slug': slug}))


class VerbalAbilityDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('VerbalAbilitymodel') and cache.get('VerbalAbilityparent_obj'):
        model = cache.get('VerbalAbilitymodel')
        parent_obj = cache.get('VerbalAbilityparent_obj')
    else:
        model = VerbalAbility
        parent_obj = VerbalAbilityParent
        cache.set('VerbalAbilitymodel', model)
        cache.set('VerbalAbilityparent_obj', parent_obj)
    like_obj = VerbalAbilityLike

    def get_context_data(self, **kwargs):
        context = super(VerbalAbilityDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Verbal Ability'
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


class InterViewQuestionView(View):
    def get(self, request):
        slug = InterviewQuestion.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:interviewquestiondetail', kwargs={'slug': slug}))


class InterviewQuestionDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('InterviewQuestionmodel') and cache.get('InterviewQuestionparent_obj'):
        model = cache.get('InterviewQuestionmodel')
        parent_obj = cache.get('InterviewQuestionparent_obj')
    else:
        model = InterviewQuestion
        parent_obj = InterviewQuestionParent
        cache.set('InterviewQuestionmodel', model)
        cache.set('InterviewQuestionparent_obj', parent_obj)
    like_obj = InterviewQuestionLike

    def get_context_data(self, **kwargs):
        context = super(InterviewQuestionDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Interview Question'
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


class CompanyQuestionView(View):
    def get(self, request):
        slug = CompanyQuestion.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:companyquestiondetail', kwargs={'slug': slug}))


class CompanyQuestionDetailView(DetailView):
    template_name = 'w3c/detail.html'
    if cache.get('CompanyQuestionmodel') and cache.get('CompanyQuestionparent_obj'):
        model = cache.get('CompanyQuestionmodel')
        parent_obj = cache.get('CompanyQuestionparent_obj')
    else:
        model = CompanyQuestion
        parent_obj = CompanyQuestionParent
        cache.set('CompanyQuestionmodel', model)
        cache.set('CompanyQuestionparent_obj', parent_obj)
    like_obj = CompanyQuestionLike

    def get_context_data(self, **kwargs):
        context = super(CompanyQuestionDetailView, self).get_context_data(**kwargs)
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
        context['title'] = 'Company Question'
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
