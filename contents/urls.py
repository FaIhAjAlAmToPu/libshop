from django.urls import path
from . import views

urlpatterns = [
    path('content/', views.content_list, name='content_list'),
    path('content/<int:pk>/', views.content_detail, name='content_detail'),

    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/isbn/<str:isbn>/', views.book_detail_by_isbn, name='book_detail_by_isbn'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/not_found/', views.book_not_found, name='book_not_found'),

    path('story/', views.story_list, name='story_list'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),

    path('search/book/', views.search_book, name='search_book'),
]
