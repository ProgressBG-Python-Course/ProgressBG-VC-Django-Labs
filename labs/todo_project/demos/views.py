from django.shortcuts import render
# from django.template import loader
from django.http import HttpResponse
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

def user(request,*args, **kwargs):
    # http://127.0.0.1:8000/demos/user/name/surname
    # http://127.0.0.1:8000/demos/user/user_id
    # => Hello <user name>

    # name = 'ivan'
    # surname = 'ivanov'

    # http://127.0.0.1:8000/demos/user/1
    # id=1


    'ivan/ivanov'
    users = {
        '1':{
            'name': 'ivan',
            'surname':'ivanov'
        }
    }

    return HttpResponse(f"""
        args: {args}<br>
        kwargs: {kwargs}<br>
        
    """)

def form(request):
    # http://127.0.0.1:8000/demos/form = show form to submit

    return render(request, 'demos/form.html', {})

def form_process(request):
    user_name = request.GET['user_name']

    return HttpResponse(f'Hello {user_name}')
