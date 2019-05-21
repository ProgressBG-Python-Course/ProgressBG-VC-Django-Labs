from rest_framework import viewsets      
from .serializers import TaskSerializer  
from todo_app.models import Task                 

class TaskView(viewsets.ModelViewSet):  
  serializer_class = TaskSerializer     
  queryset = Task.objects.all()         