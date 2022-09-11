# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import *

urlpatterns = [

    # The home page
    path('dashboard/', index, name='home'),
    path('', h, name='h'),

    # Matches any html file
    re_path(r'^.*\.*', pages, name='pages'),

]
