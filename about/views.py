# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Skill, ContactDetails
# Create your views here.

def get_about(request):
    skills = Skill.objects.all()
    return render(request, 'about/about.html', {'skills':skills})


def get_contact(request):
    contact = ContactDetails.objects.all()
    return render(request, 'about/contact.html', {'contact': contact})