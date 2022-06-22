from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import *


# Create your views here.
class IndexView(TemplateView):
    template_name = 'w3c/index.html'
