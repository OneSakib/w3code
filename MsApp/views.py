from django.shortcuts import HttpResponseRedirect
from django.views.generic import View, DetailView
from .models import *
from next_prev import prev_in_order, next_in_order


# Create your views here.
class MSExcelView(View):
    def get(self, request):
        slug = MSExcel.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('MS:msexceldetail', kwargs={'slug': slug}))


class MSExcelDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = MSExcel

    def get_context_data(self, **kwargs):
        context = super(MSExcelDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'MS Excel'
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


class MSWordView(View):
    def get(self, request):
        slug = MSWord.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('MS:msworddetail', kwargs={'slug': slug}))


class MSWordDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = MSWord

    def get_context_data(self, **kwargs):
        context = super(MSWordDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'MS Word'
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



class MSPowerpointView(View):
    def get(self, request):
        slug = MSPowerpoint.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('MS:mspowerpointdetail', kwargs={'slug': slug}))


class MSPowerpointDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = MSPowerpoint

    def get_context_data(self, **kwargs):
        context = super(MSPowerpointDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'MS Powerpoint'
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



class MSOneNoteView(View):
    def get(self, request):
        slug = MSOneNote.objects.first().slug
        return HttpResponseRedirect(reverse_lazy('MS:msonenotedetail', kwargs={'slug': slug}))


class MSOneNoteDetailView(DetailView):
    template_name = 'w3c/detail.html'
    model = MSOneNote

    def get_context_data(self, **kwargs):
        context = super(MSOneNoteDetailView, self).get_context_data(**kwargs)
        obj_list = self.model.objects.all()
        context['obj_list'] = obj_list
        context['title'] = 'MS One Note'
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
