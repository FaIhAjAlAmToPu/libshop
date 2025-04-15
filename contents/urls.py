from django.urls import path
from . import views

urlpatterns = [
    path('content/', views.content_list, name='content_list'),
    path('content/<int:pk>/', views.content_detail, name='content_detail'),

    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),

    path('story/', views.story_list, name='story_list'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),
]
