from django.urls import path, include            
from rest_framework import routers               
from . import views                              

router = routers.DefaultRouter()                   
# router.register(r'todos', views.TaskView, 'todo')  

# http://127.0.0.1:8000/api/tasks/
urlpatterns = [
  path('tasks/', views.getTodos, name='todos')       
  # path('tasks/<id>', views.getTodos, name='todos')       
]
