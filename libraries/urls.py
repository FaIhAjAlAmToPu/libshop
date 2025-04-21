from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/store/', views.register_store, name='register_store'),
    path('stores/', views.stores, name='stores'),
    path('stores/near/', views.stores_near, name='stores_near'),
    path('save_location/', views.set_location, name='set_location'),

    path('stores', views.store_detail, name='store_detail'),
    path('search/store/', views.search_store, name='search_store'),
    path('search/store_content/', views.search_store_content, name='search_store_content'),
    path('search/near_store_content/', views.search_near_store_content, name='search_near_store_content'),

path('store_content/<int:store_content_id>/', views.store_content_detail, name='store_content_detail'),
]