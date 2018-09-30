# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Skill
# Create your views here.

def get_about(request):
    skills = Skill.objects.all()
    return render(request, 'about/about.html', {'skills':skills})


