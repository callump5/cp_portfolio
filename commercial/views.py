# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from portfolio.models import Project, JobRequirement

# Create your views here.

def get_commercial(request):
    job_reqs = JobRequirement.objects.all()
    projects = Project.objects.all()
    return render(request, 'commercial/home.html', {'projects': projects,
                                                    'job_reqs':job_reqs})
