from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# print(f'########: {auth_views.__dir__()}')

urlpatterns = [
  path('login', auth_views.LoginView, name="login"),
  path('create_user', views.create_user, name="create_user"),
  path('change_password', views.change_password, name="change_password"),
  path('auth_user', views.auth_user, name="auth_user"),
]