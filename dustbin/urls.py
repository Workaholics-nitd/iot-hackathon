"""dustbin URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from datavis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datavis/0/', views.get_percentage, name='datavis'),
    path('get_val/', views.get_percentage_value, name='get_val'),
    path('datavis/', views.all_dustbins, name='datavis'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('locations/', views.locations, name='locations'),
    path('datavis/add_comment/', views.add_comment, name='add_comment'),
]
