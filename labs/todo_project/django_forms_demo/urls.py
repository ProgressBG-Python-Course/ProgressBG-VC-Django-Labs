from django.urls import path
from . import views

urlpatterns = [
  # 127.0.0.1:8000/forms
  path('', views.list_tasks, name="django_forms_demo_list_tasks"),
  path('create_task', views.create_task, name="django_forms_demo_create_task"),
  path('delete_task/<int:id>', views.delete_task, name="django_forms_demo_delete_task"),
  path('update_task/<int:id>', views.update_task, name="django_forms_demo_update_task"),
]