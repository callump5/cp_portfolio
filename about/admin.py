# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Skill, Category, ContactDetails

# Register your models here.

admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(ContactDetails)