from django.urls import path

from .views import index

urlpatterns = [

    # The home page
    path('projectos/', index, name='projectos_list'),

]