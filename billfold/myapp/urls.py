from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('delete/<str:pk>', views.deleteview, name = 'delete'),
    path('wallets', views.walletsview, name = 'wallets'),
    path('wallet/<str:pk>/', views.walletview, name = 'wallet')
]
