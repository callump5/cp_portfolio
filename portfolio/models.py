# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField


from .upload_to_aws import upload_img
# Create your models here.

class JobRequirement(models.Model):
    job_requirement = models.CharField(max_length=200)
    description = HTMLField()

    def __unicode__(self):
        return self.job_requirement



class Project(models.Model):

    project = models.CharField(max_length=200)
    slug = models.SlugField()
    project_logo = models.ImageField(upload_to=upload_img)
    description = HTMLField()
    job_requirements = models.ManyToManyField(JobRequirement)
    website =  models.CharField(max_length=200)
    github =  models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    testimonial = HTMLField()


    def __unicode__(self):
        return self.project