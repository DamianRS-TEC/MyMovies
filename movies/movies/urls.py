"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mymovies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('tail', views.tail, name='tail'),
    path('tail2', views.tail2, name='tail2'),
    path('tail3', views.tail3, name='tail3'),
    path('tail4', views.tail4, name='tail4'),
    path('tail5', views.tail5, name='tail5'),
    path('tail6', views.tail6, name='tail6'),
]
