from django.urls import path
from . import views

urlpatterns = [
  # 127.0.0.1:8000/forms
  path('', views.list_tasks, name="list_tasks"),
  path('create_task', views.create_task, name="create_task"),
  path('delete_task/<int:id>', views.delete_task, name="delete_task"),
  path('update_task/<int:id>', views.update_task, name="update_task"),
]