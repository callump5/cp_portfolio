# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-30 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.TextField(default='www.awdawf.co.uk'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='website',
            field=models.TextField(default='www.awdawf.co.uk'),
            preserve_default=False,
        ),
    ]