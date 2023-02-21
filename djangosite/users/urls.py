from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm
from users.views import *

urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',
                                              form_class=UserPasswordResetForm), name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
