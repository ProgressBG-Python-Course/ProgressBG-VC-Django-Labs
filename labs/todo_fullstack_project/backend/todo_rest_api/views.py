from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
# views should return JSON

# [GET]http://127.0.0.1:8000/api/tasks/ => Read Todos
# [POST]http://127.0.0.1:8000/api/tasks/ => Create Todo
# [PUT]http://127.0.0.1:8000/api/tasks/id => Update Todo
# [DELETE]http://127.0.0.1:8000/api/tasks/id => Delete Todo

# http://127.0.0.1:8000/api/tasks/
def getTodos(request):
  if request.method == 'GET':
    # get all todos from dd
    todos = Task.objects.all()

    # serialize as JSON

    # return HTTPJSON

  if request.method == 'POST':
    pass

# def updateTodo(request, id=id){  
# }


