from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.models import Task
import datetime


app_name = 'HTML forms in Django'
# http://127.0.0.1:8000
def list_tasks(request): 
    tasks = Task.objects.all()
    template_file = 'list_tasks.html'

    context = {
        'tasks': tasks,
        'app_name': app_name,         
        'page_name': 'list_tasks'       
    }

    return render(request, template_file, context)

# http://127.0.0.1:8000/create_task
def create_task(request):  
  now = datetime.datetime.now()

  # create or update (discus on ORM topics)
  # obj_task, created = Task.objects.update_or_create(id=id, defaults=values_to_update)

  Task.objects.create(
    title = request.POST.get('title'),
    description = request.POST.get('description','default description'),
    due = datetime.datetime.strptime(request.POST.get('due'), '%Y-%m-%d')    
  )
  
  return redirect('list_tasks')

def update_task(request,id):
  if request.method == "POST":
    # form data is submited => save it to DB
    task = Task.objects.filter(id=id).update(
      title = request.POST.get('title'),
      description = request.POST.get('description','default description'),
      due = datetime.datetime.strptime(request.POST.get('due'), '%Y-%m-%d') 
    ) 
    return redirect('list_tasks')
  else: 
    # render the update form:
    task = Task.objects.get(id=id)

    template_file = 'update_task.html'

    context = {
        'task': task,
        'app_name': app_name,         
        'page_name': 'update_task'       
    }

    return render(request, template_file, context)


def delete_task(request,id):
  Task.objects.filter(id=id).delete()
  
  return redirect('list_tasks')