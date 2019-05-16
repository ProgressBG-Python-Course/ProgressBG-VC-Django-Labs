from django.urls import path
from . import views

urlpatterns = [
  path('create_user', views.create_user, name="create_user"),
  path('change_password', views.change_password, name="change_password"),
  path('auth_user', views.auth_user, name="auth_user"),
]