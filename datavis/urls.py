from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_percentage, name='get_percentage'),
    path(
        'get_percentage_value',
        views.get_percentage_value,
        name='get_percentage_value',
    ),
    path('locations', views.locations, name='locations'),
]
