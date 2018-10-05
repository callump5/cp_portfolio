# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from portfolio.models import Project, JobRequirement
from .forms import BookingForm

# Create your views here.

def get_commercial(request):
    job_reqs = JobRequirement.objects.all()
    projects = Project.objects.all()[0:3]


    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'commercial/home.html', {'projects': projects,
                                                    'job_reqs':job_reqs,
                                                    'form': form})
