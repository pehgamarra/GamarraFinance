from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, user_login, logged_in

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logged_in/', logged_in, name='logged_in'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
