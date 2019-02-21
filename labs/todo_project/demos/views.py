from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
from todo_app.models import Task

# Create your views here.
def list(request):
    latest_tasks = Task.objects.order_by('due')[:5]

    context = {
    	'title': "Latest Tasks",
        'latest_tasks': latest_tasks
    }

    template_file = 'demos/list.html'


    return render(request, template_file, context)

def table(request):
    latest_tasks = Task.objects.order_by('due')[:5]

    context = {
        'latest_tasks': latest_tasks
    }

    template_file = 'demos/table.html'


    return render(request, template_file, context)

def task(request, id):
    print(f"id: {id}")
    task = Task.objects.get(id=id)

    context = {
        'task': task
    }

    template_file = 'demos/task.html'


    return render(request, template_file, context)
