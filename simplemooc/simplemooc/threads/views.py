from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Thread

#class ThreadView(View):
#    def get(self, request, *args, **kwargs):
#    	return render(request, 'threads/index.html')


class ThreadView(ListView):
    model = Thread
    paginate_by = 10
    template_name = 'threads/index.html'

    def get_context_data(self, **kwargs):
    	context = super(ThreadView, self).get_context_data(**kwargs)
    	context['tags'] = Thread.tags.all()
    	return context

index = ThreadView.as_view()