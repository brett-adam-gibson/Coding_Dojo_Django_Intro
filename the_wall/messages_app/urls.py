from django.urls import path
from . import views


urlpatterns = [
    #localhost:8000/posts
    path('', views.the_wall),
    #localhost:8000/posts/create_post
    path('create_post', views.create_posts),
    #localhost:8000/posts/1/delete
    path('<int:post_id>/delete', views.delete_post),
    path('add_comment/<int:post_id>', views.add_comment),
]
