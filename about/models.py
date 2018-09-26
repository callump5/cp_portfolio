# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __unicode__(self):
        return self.category

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    description = HTMLField()
    category = models.ForeignKey(Category, related_name='skill_category')

    def __unicode__(self):
        return self.skill