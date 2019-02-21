from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
from todo_app.models import Task

# Create your views here.
def index(request):
    latest_tasks = Task.objects.order_by('due')[:5]

    context = {
        'latest_tasks': latest_tasks
    }

    template_file = 'todo_app/index.html'


    return render(request, template_file, context)

# http://127.0.0.1:8000/list
def list(request):
    latest_tasks = Task.objects.order_by('due')[:5]

    context = {
        'latest_tasks': latest_tasks
    }

    template_file = 'todo_app/list.html'


    return render(request, template_file, context)
