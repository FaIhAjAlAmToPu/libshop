from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/store/', views.register_store, name='register_store'),
    path('stores/', views.stores, name='stores'),
    path('stores/near/', views.stores_near, name='stores_near'),
    path('store/', views.store_detail, name='store_detail'),
]