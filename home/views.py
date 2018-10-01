# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import datetime
# Create your views here.


def get_home(request):
    now = datetime.datetime.now()
    return render(request, 'personal/home/home.html', {'now': now})