from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('ais/<int:ai_id>/', views.ai_detail, name='ai_detail'),
    path('ais/', views.ais, name="ais"),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/', views.books, name="books"),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('authors/', views.authors, name="authors"),
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),
    path('series/', views.series, name="series"),
]