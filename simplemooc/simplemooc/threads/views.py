from django.shortcuts import render
from django.views.generic import TemplateView


class ThreadView(TemplateView):
    template_name = 'threads/index.html'


index = ThreadView.as_view()
index = ThreadView.as_view(template_name='threads/index.html')