from django.urls import path
from . import views

urlpatterns = [
    #localhost:8000/fav_books/
    path('', views.fav_books),
    #localhost:8000/fav_books/add_fav_book
    path('add_fav_book', views.add_fav_book),
    path('<int:book_id>', views.view_book),
    #localhost:8000/fav_books/logout
    path('logout', views.logout),
    path("favorite/<int:book_id>", views.favorite),
    path("unfavorite/<int:book_id>", views.unfavorite),
]
