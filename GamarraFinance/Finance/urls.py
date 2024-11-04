from django.urls import path
from .views import register, user_login, logged_in

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logged_in/', logged_in, name='logged_in'),
]
