"""covidproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from covidapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('covidapp.urls')),
    path('', views.indexPage, name='index'),
    #path('userlocation', views.userlocation, name='userlocation'), # This tells Django to search for URL patterns in the file covidapp/urls.py. So we create urls.py in app
]
