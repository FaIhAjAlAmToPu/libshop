from django.urls import path, include
from users import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.CustomLoginView.as_view(), name='login'),
]
