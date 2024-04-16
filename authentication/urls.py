from django.urls import path, include
from django.contrib import admin
from . import views
from .views import upload_information
from authentication import views

urlpatterns = [

    path('', views.login_view, name='login'),
    path('index', views.index, name='index'),
    path('upload_information', views.upload_information, name='upload_information'),
]
