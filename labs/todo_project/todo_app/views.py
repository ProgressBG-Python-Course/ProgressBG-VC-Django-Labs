from django.shortcuts import render, redirect
# from django.template import loader
from django.http import HttpResponse
from todo_app.models import Task


# Create your views here.
def index(request): 
    tasks = Task.objects.all()

    template_file = 'todo_app/index.html'

    context = {
        'tasks': tasks,
        'app_name': 'Todo App', 
        'page_name': 'index'       
    }


    return render(request, template_file, context)

# http://127.0.0.1:8000/list
def list(request):
    import datetime
    
    now = datetime.datetime.now()
    
    template_file = 'todo_app/list.html'

    # return HttpResponse('OK')

    return render(request, template_file, {'now':now})

def table(request):
    latest_tasks = Task.objects.order_by('due')[:5]

    context = {
        'latest_tasks': latest_tasks
    }

    template_file = 'todo_app/table.html'


    return render(request, template_file, context)

def delete(request, **kwargs):    
    tasks = Task.objects.all()    

    template_file = 'todo_app/index.html'


    if request.method == 'GET':
        item_id = request.GET['id']        
    else:
        item_id = kwargs['id']

    context = {
        'tasks': tasks,
        'app_name': 'Todo App', 
        'page_name': 'delete', 
        # TODO_DONE     
        'item_id': int(item_id)     
    }

        
    return render(request, template_file, context)

def edit(request, **kwargs):
    item_id = kwargs['id']

    tasks = Task.objects.all()

    template_file = 'todo_app/edit.html'

    context = {
        'tasks': tasks,
        'app_name': 'Todo App', 
        'page_name': 'edit',      
        'item_id': item_id     
    }

        
    return render(request, template_file, context)

# delete({}, id=2)