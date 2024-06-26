from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from .views import RegisterView, ProfileView, email_verification, ResetView, PasswordResetDone, ResetConfirmView, \
    ResetCompleteView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/password_reset/', ResetView.as_view(), name='password_reset'),
    path('done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetConfirmView.as_view(), name='password_confirm'),
    path('users/reset/compete/', ResetCompleteView.as_view(), name='complete'),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
]
