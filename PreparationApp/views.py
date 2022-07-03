from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import next_in_order, prev_in_order


# Create your views here.
class AptitudeView(View):
    def get(self, request):
        slug = Aptitude.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:aptitudedetail', kwargs={'slug': slug}))


class AptitudeDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Aptitude

    def get_context_data(self, **kwargs):
        context = super(AptitudeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Aptitude'
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



class ReasoningView(View):
    def get(self, request):
        slug = Reasoning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:reasoningdetail', kwargs={'slug': slug}))


class ReasoningDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = Reasoning

    def get_context_data(self, **kwargs):
        context = super(ReasoningDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Reasoning'
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



class VerbalAbilityView(View):
    def get(self, request):
        slug = VerbalAbility.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:verbalabilitydetail', kwargs={'slug': slug}))


class VerbalAbilityDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = VerbalAbility

    def get_context_data(self, **kwargs):
        context = super(VerbalAbilityDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Verbal Ability'
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



class InterViewQuestionView(View):
    def get(self, request):
        slug = InterviewQuestion.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:interviewquestiondetail', kwargs={'slug': slug}))


class InterviewQuestionDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = InterviewQuestion

    def get_context_data(self, **kwargs):
        context = super(InterviewQuestionDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Interview Question'
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


class CompanyQuestionView(View):
    def get(self, request):
        slug = CompanyQuestion.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:companyquestiondetail', kwargs={'slug': slug}))


class CompanyQuestionDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = CompanyQuestion

    def get_context_data(self, **kwargs):
        context = super(CompanyQuestionDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'Company Question'
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

