# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-30 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import portfolio.upload_to_aws


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20180930_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_logo',
            field=models.ImageField(upload_to=portfolio.upload_to_aws.upload_img),
        ),
    ]
