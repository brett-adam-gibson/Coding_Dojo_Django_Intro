from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('<int:course_id>/delete', views.delete),
    path('<int:course_id>', views.comments),
    path('<int:course_id>/comments', views.create_comments),
]
