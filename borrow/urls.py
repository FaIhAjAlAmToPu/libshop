from django.urls import path
from . import views

urlpatterns = [
    path('borrow_request/', views.borrow_request, name='borrow_request'),
    path('borrow/', views.borrow, name='borrow'),
    path('borrowed/', views.borrowed, name='borrowed'),
]