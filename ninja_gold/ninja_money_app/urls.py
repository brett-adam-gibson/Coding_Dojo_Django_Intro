from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('process_money', views.process_money),
    path('reset', views.reset),
]


# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^process_money$', views.process_money),
#     url(r'^reset$', views.reset),
# ]