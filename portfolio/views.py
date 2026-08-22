from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.order_by('-created_at')[:3]
    return render(request, 'portfolio/home.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact(request):
    return render(request, 'portfolio/contact.html')