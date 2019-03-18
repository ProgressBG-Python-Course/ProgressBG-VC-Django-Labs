from django.urls import path
from . import views

urlpatterns = [
  # /todos/ => list all tasks
  path('', views.index, name="todo_index"),

  # /todos/add => add a tasks
  path('add', views.add, name="todo_add"),

  # /todos/update/1 => update task with given id
  path('update/<int:id>', views.update, name="todo_update"),
 
  # /todos/delete/1 => delete task with given id
  path('delete/<int:id>', views.delete, name="todo_delete"),

  # /todos/complete/1 => set as complete the task with given id
  path('complete/<int:id>', views.complete, name="todo_complete"),

]