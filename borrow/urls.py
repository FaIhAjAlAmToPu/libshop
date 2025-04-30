# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('request/<int:store_content_id>/', views.send_borrow_request, name='send_borrow_request'),
    path('requests/', views.view_borrow_requests, name='view_borrow_requests'),
    path('requests/<int:request_id>/approve/', views.approve_borrow_request, name='approve_borrow_request'),
    path('requests/<int:request_id>/reject/', views.reject_borrow_request, name='reject_borrow_request'),
    path('list/', views.my_borrowed_books, name='my_borrowed_books'),
    path('return/<int:borrow_id>/', views.mark_returned, name='mark_returned'),
]
