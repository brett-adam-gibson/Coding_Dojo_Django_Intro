from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_register),
    path('create_user', views.create_user),
    path('login', views.login),
]
