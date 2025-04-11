from django.urls import path, include
from libraries import views
urlpatterns = [
    path('', views.home, name='home'),
]
