from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.models import Task


# http://127.0.0.1:8000
def list_tasks(request): 
    tasks = Task.objects.all()
    template_file = 'list_tasks.html'

    context = {
        'tasks': tasks,
        'app_name': 'Forms demo',         
        'page_name': 'list_tasks'       
    }

    return render(request, template_file, context)

# http://127.0.0.1:8000/create_task
def create_task(request):
  import datetime
  now = datetime.datetime.now()

  # create or update...
  # obj_task, created = Task.objects.update_or_create(id=id, defaults=values_to_update)


  Task.objects.create(
    title = request.GET['title'],
    description = request.GET.get('description','default description'),
    # created = datetime.datetime.strptime(request.GET['created'], '%YYYY-%mm-%d'),
    # due = datetime.datetime.strptime(due)
    created = now,
    due = now + datetime.timedelta(days=1),
    end = now + + datetime.timedelta(days=3),
  )
  
  return redirect('list_tasks')

def delete_task(request,id):
  Task.objects.filter(id=id).delete()
  
  return redirect('list_tasks')

def update_task(request,id):
  task = Task.objects.get(id=id)  

  template_file = 'update_task.html'

  context = {
      'task': task,
      'app_name': 'Forms demo',         
      'page_name': 'update_task'       
  }

  return render(request, template_file, context)