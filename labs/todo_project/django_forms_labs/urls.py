from django.urls import path
from . import views

urlpatterns = [
  path('', views.list_tasks, name="django_forms_labs_list_tasks"),
  path('create_task', views.create_task, name="django_forms_labs_create_task"),
  path('delete_task/<int:id>', views.delete_task, name="django_forms_labs_delete_task"),
  path('update_task/<int:id>', views.update_task, name="django_forms_labs_update_task"),
]