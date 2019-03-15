from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.timezone import make_aware
from todo_app.models import Task
from django.forms.models import model_to_dict
import datetime
from .forms import CreateTaskForm, UpdateTaskForm


app_name = 'Django Forms Demo'
def list_tasks(request): 
    tasks = Task.objects.all()
    template_file = 'django_forms_demo/list_tasks.html'

    context = {
        'tasks': tasks,
        'form': CreateTaskForm,
        'app_name': app_name,         
        'page_name': 'list_tasks'       
    }

    return render(request, template_file, context)

def create_task(request):  
  now = datetime.datetime.now()

  # create or update (discus on ORM topics)
  # obj_task, created = Task.objects.update_or_create(id=id, defaults=values_to_update)

  Task.objects.create(
    title = request.POST.get('title'),
    description = request.POST.get('description','default description'),
    due = make_aware(datetime.datetime.strptime(request.POST.get('due'), '%Y-%m-%d'))
  )
  
  return redirect('django_forms_demo_list_tasks')

def update_task(request,id):
  if request.method == "POST":
    # form data is submited
    print(request.POST)

    form = UpdateTaskForm(request.POST)
    
    if form.is_valid:        
      # if data is valid => save it to DB
      task = Task.objects.filter(id=id).update(
        title = request.POST.get('title'),
        description = request.POST.get('description','default description'),
        due = make_aware(datetime.datetime.strptime(request.POST.get('due'), '%Y-%m-%d')) 
      ) 
      return redirect('django_forms_demo_list_tasks')
  else: 
    # render the update form:
    task = Task.objects.get(id=id)

    # form = UpdateTaskForm({
    #   'title': task.title,
    #   'description': task.description,
    #   'due': task.due
    # })
    form = UpdateTaskForm(model_to_dict(task))    

    template_file = 'django_forms_demo/update_task.html'

    context = {
        'task': task,
        'form': form,
        'app_name': app_name,         
        'page_name': 'update_task'       
    }

    return render(request, template_file, context)


def delete_task(request,id):
  Task.objects.filter(id=id).delete()
  
  return redirect('django_forms_demo_list_tasks')