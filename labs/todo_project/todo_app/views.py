from django.shortcuts import render, redirect
# from django.template import loader
from django.http import HttpResponse
from todo_app.models import Task


# /todos/ => list all tasks
def index(request):     
    tasks = Task.objects.order_by('id')

    # form = TaksForm()

    template_file = 'todo_app/index.html'

    context = {
        'tasks': tasks,
        'app_name': 'Todo App', 
        'page_name': 'index'       
    }


    return render(request, template_file, context)


# /todos/add => add a tasks
def add(request): 
    # all processing should happen only when the request method is POST
    if request.method == 'POST':
        new_task = Task(title=request.POST['task_title'])
        new_task.save()

        return redirect('index')

    elif request.method == 'GET':
        return HttpResponse('Error: GET method is not allowed for /add')
    else:
        return HttpResponse(f'Unknown method {request.method} ') 


def delete(request, id, **kwargs):          

    Task.objects.filter(id=id).delete()

    return redirect('index')

def complete(request, id): 
    task = Task.objects.get(id=id)
    if task.completed:
        task.completed = False
    else:
        task.completed = True

    task.save()

    return redirect('index')

def edit(request, id,  **kwargs):
    return HttpResponse('Edit task')

