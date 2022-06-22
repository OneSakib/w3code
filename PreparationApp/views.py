from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, FormView, DetailView
from .models import *
from .forms import *
from next_prev import next_in_order, prev_in_order


# Create your views here.
class AptitudeView(View):
    def get(self, request):
        slug = Aptitude.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:aptitudedetail', kwargs={'slug': slug}))


class AptitudeDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = AptitudeCommentsForm
    model = Aptitude

    def get_context_data(self, **kwargs):
        context = super(AptitudeDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = AptitudeComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Preparation:aptitudedetail', kwargs={'slug': self.kwargs['slug']}))


class ReasoningView(View):
    def get(self, request):
        slug = Reasoning.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:reasoningdetail', kwargs={'slug': slug}))


class ReasoningDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = ReasoningCommentsForm
    model = Reasoning

    def get_context_data(self, **kwargs):
        context = super(ReasoningDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = ReasoningComments.objects.filter(post=self.object)
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
        return HttpResponseRedirect(reverse_lazy('Preparation:reasoningdetail', kwargs={'slug': self.kwargs['slug']}))


class VerbalAbilityView(View):
    def get(self, request):
        slug = VerbalAbility.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:verbalabilitydetail', kwargs={'slug': slug}))


class VerbalAbilityDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = VerbalAbilityCommentsForm
    model = VerbalAbility

    def get_context_data(self, **kwargs):
        context = super(VerbalAbilityDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = VerbalAbilityComments.objects.filter(post=self.object)
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
            reverse_lazy('Preparation:verbalabilitydetail', kwargs={'slug': self.kwargs['slug']}))


class InterViewQuestionView(View):
    def get(self, request):
        slug = InterviewQuestion.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:interviewquestiondetail', kwargs={'slug': slug}))


class InterviewQuestionDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = InterviewQuestionCommentsForm
    model = InterviewQuestion

    def get_context_data(self, **kwargs):
        context = super(InterviewQuestionDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = InterviewQuestionComments.objects.filter(post=self.object)
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
            reverse_lazy('Preparation:interviewquestiondetail', kwargs={'slug': self.kwargs['slug']}))


class CompanyQuestionView(View):
    def get(self, request):
        slug = CompanyQuestion.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('Preparation:companyquestiondetail', kwargs={'slug': slug}))


class CompanyQuestionDetailView(DetailView, FormView):
    template_name = 'db/detail.html'
    form_class = CompanyQuestionCommentsForm
    model = CompanyQuestion

    def get_context_data(self, **kwargs):
        context = super(CompanyQuestionDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['comments'] = CompanyQuestionComments.objects.filter(post=self.object)
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
            reverse_lazy('Preparation:companyquestiondetail', kwargs={'slug': self.kwargs['slug']}))
