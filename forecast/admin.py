# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import wheather, userprofile

admin.site.register(wheather)
admin.site.register(userprofile)

