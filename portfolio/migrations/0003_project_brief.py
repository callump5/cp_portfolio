# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-29 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20180929_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='brief',
            field=models.CharField(default='django project with AWS integration', max_length=250),
            preserve_default=False,
        ),
    ]
