from django.urls import path
from . import views
urlpatterns = [
    #this is localhost:800-/random/
    path('', views.random),
    path('random_word', views.random),
    path('reset', views.reset),
]
