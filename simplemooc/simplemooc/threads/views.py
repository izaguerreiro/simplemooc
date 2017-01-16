from django.shortcuts import render
from django.views.generic import TemplateView


class ThreadView(TemplateView):
    template_name = 'threads/index.html'