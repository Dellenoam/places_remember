from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
