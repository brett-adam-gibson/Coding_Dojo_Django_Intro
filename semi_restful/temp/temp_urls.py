from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/shows
    path('', views.index),
    # localhost:8000/shows/new
    path('new', views.new),
    # localhost:8000/shows/create
    path('create', views.create),
    # localhost:8000/shows/<show_id>/edit
    path('<int:show_id>/edit', views.edit),
    # localhost:8000/shows/<show_id>/update
    path('<int:show_id>/update', views.update),
    # localhost:8000/shows/<show_id>
    path('<int:show_id>', views.show),
    # localhost:8000/shows/<show_id>/delete
    path('<int:show_id>/delete', views.delete),

]

# Ask Devon timestamp 14:05 (in), fg:text (form-group), also ask about muli word edit keybord shortcut
