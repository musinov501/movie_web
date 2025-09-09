from collections import namedtuple

from django.urls import path
from .views import home, movie_by_category, show_in_detail, save_comment, save_movies, update_movies, delete_movies

urlpatterns = [
    path('', home, name= 'home'),
    path('genre/<int:genre_id>/', movie_by_category, name ="by_genre"),
    path('movie/add/', save_movies, name= 'add_movie'),
    path('movie/<int:pk>/', show_in_detail, name = "show_detail"),
    path('movie/<int:pk>/update/', update_movies, name = 'update_movies'),
    path('movie/<int:pk>/delete/', delete_movies, name = 'delete_movie'),
    path('news/comment/add/<int:movie_id>/', save_comment, name= 'add_comment')
]


