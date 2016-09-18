from django.shortcuts import render, get_object_or_404
from .models import Course


def index(request):
    template_name = 'courses/index.html'
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, template_name, context)


def details(request, pk):
    template_name = 'courses/details.html'
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}    
    return render(request, template_name, context)
