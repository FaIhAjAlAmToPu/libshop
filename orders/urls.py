from django.urls import path
from . import views

urlpatterns = [
    path('buy/', views.buy, name='buy'),
    path('bought/', views.bought, name='bought'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:store_content_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/done/', views.checkout_done, name='checkout_done'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('checkout/error/', views.checkout_error, name='checkout_error'),
    path('checkout/cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('requests/', views.order_requests, name='order_requests'),
    path('history/', views.order_history, name='order_history'),
    path('detail/<int:pk>/', views.order_detail, name='order_detail'),
    path('requests/<int:pk>/accept/', views.accept_order_requests, name='accept_order_requests'),
]