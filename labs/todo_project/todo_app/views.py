from django.shortcuts import render
# from django.template import loader
from django.http import HttpResponse
from todo_app.models import Task

# Create your views here.
def index(request):
   	

    template_file = 'todo_app/index.html'

    context = {
        'page_title': 'Todo App Index'
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
