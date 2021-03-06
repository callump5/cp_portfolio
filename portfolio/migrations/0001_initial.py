# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import portfolio.upload_to_aws
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_requirement', models.CharField(max_length=200)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('project_logo', models.ImageField(upload_to=portfolio.upload_to_aws.upload_img)),
                ('description', tinymce.models.HTMLField()),
                ('website', models.CharField(max_length=200)),
                ('github', models.CharField(max_length=200)),
                ('client', models.CharField(max_length=200)),
                ('testimonial', tinymce.models.HTMLField()),
                ('job_requirements', models.ManyToManyField(to='portfolio.JobRequirement')),
            ],
        ),
    ]
