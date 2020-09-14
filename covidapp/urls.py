from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name = 'index'),
    #path('userlocation', views.userlocation, name = 'userlocation'),
    #url(r'arena/$', views.arena, name='arena'),
]