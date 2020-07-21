from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('<int:user_id>', views.show)
]
