from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('reset-password/', views.password_reset_view, name='password_reset'),
    path('reset-password/<uidb64>/<token>/', views.password_reset_confirm_view,
         name='password_reset_confirm'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
