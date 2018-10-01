# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Project

# Create your views here.

def get_portfolio(request):
    projects = Project.objects.all()
    return render(request, 'personal/portfolio/projects.html', {'projects': projects})

def get_project(request, slug):
    project = Project.objects.get(slug__exact=slug)
    return render(request, 'personal/portfolio/project.html', {'project': project})
