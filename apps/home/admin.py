# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from apps.home.models import Perguntas, SobreNos

# Register your models here.

admin.site.register(Perguntas)
admin.site.register(SobreNos)
