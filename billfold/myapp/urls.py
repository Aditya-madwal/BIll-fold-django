from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeview, name = 'home'),
    path('delete/<str:pk>', views.deleteview, name = 'delete')
]
