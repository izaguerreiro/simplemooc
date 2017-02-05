from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Thread

#class ThreadView(View):
#    def get(self, request, *args, **kwargs):
#    	return render(request, 'threads/index.html')


class ThreadListView(ListView):
    paginate_by = 10
    template_name = 'threads/index.html'

    def get_queryset(self):
    	queryset = Thread.objects.all()
    	order = self.request.GET.get('order', '')
    	if order == 'views':
    		queryset = queryset.order_by('-views')
    	elif order == 'answers':
    		queryset = queryset.order_by('-answers')
    	tag = self.kwargs.get('tags', '')
    	if tag:
    		queryset = queryset.filter(tags__slug__icontains=tag)
    		print(queryset)
    	return queryset

    def get_context_data(self, **kwargs):
    	context = super(ThreadListView, self).get_context_data(**kwargs)
    	context['tags'] = Thread.tags.all()
    	return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread.html'


index = ThreadListView.as_view()
thread = ThreadDetailView.as_view()