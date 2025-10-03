from django.shortcuts import render

from django.shortcuts import render
from .models import Skill, Experience, Project

def index(request):
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    return render(request, "index.html", {
        "skills": skills,
        "experiences": experiences,
        "projects": projects[:3],
    })

def archive(request):
    projects = Project.objects.all()
    return render(request, "archive.html", {
        "projects": projects[:3],
    })
    
from django.http import FileResponse, Http404

def resume(request):
    return FileResponse(open('theme/templates/Fayez_Al-Shwayya_CV.pdf', 'rb'), content_type='application/pdf')
