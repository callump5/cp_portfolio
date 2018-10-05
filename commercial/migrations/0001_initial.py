# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 00:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of booking', verbose_name='Day of booking')),
                ('start_time', models.TimeField(choices=[(datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM'), (datetime.time(13, 0), '1 PM'), (datetime.time(14, 0), '2 PM'), (datetime.time(15, 0), '3 PM'), (datetime.time(16, 0), '4 PM'), (datetime.time(17, 0), '5 PM')], help_text='Booking slot', max_length=200, verbose_name='Booking slot')),
                ('end_time', models.TimeField(choices=[(datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 PM'), (datetime.time(13, 0), '1 PM'), (datetime.time(14, 0), '2 PM'), (datetime.time(15, 0), '3 PM'), (datetime.time(16, 0), '4 PM'), (datetime.time(17, 0), '5 PM')], help_text='Finish Time', max_length=200, verbose_name='Finish time')),
                ('notes', models.TextField(blank=True, help_text='Notes', null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Booking',
            },
        ),
    ]
