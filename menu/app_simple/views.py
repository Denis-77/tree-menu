from django.shortcuts import render
from django.views.generic.base import TemplateView


class MainView(TemplateView):
    template_name = 'app_simple/index.html'

