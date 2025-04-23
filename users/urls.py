from django.urls import path, include
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('profile/<int:pk>/', views.user_profile, name='user_profile'),
]
