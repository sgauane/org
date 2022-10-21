from django.urls import path
from .views import *

urlpatterns = [

    # The home page
    path('projectos/', index, name='projectos_list'),

]