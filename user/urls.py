# user/urls.py
from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile_update/<int:pk>/', ProfileUpdate.as_view(), name='profile-update'),
]
