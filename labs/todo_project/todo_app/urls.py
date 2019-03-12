from django.urls import path
from . import views

urlpatterns = [
  # /todos/ => list all tasks
  path('', views.index, name="index"),

  # /todos/add => add a tasks
  path('add', views.add, name="add"),

  # /todos/edit/1 => edit task with given id
  path('edit/<int:id>', views.edit, name="edit"),
 
  # /todos/delete/1 => delete task with given id
  path('delete/<int:id>', views.delete, name="delete"),

  # /todos/complete/1 => set as complete the task with given id
  path('complete/<int:id>', views.complete, name="complete"),

]