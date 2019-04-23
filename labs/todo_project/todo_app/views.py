from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.utils.timezone import make_aware

import datetime

from todo_app.models import Task
from todo_app.forms import CreateUpdateTaskForm


app_name="Todo App"
due_date_format = "%Y-%m-%dT%H:%M"

# /todos/ => list all tasks
def index(request):
    tasks = Task.objects.order_by('id')

    # form = TaksForm()

    template_file = 'todo_app/index.html'

    context = {
        'form': CreateUpdateTaskForm,
        'tasks': tasks,
        'app_name': 'Todo App', 
        'page_name': 'index'
    }


    return render(request, template_file, context)


# /todos/add => add a tasks
def add(request): 
    # save the filled form data to DB:
    if request.method == 'POST':       
      form = CreateUpdateTaskForm(request.POST)

      if form.is_valid(): 
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']

        if request.POST.get('due', None):
          due = form.cleaned_data['due']
        else:
          due= make_aware(datetime.datetime.now() + datetime.timedelta(days=1))

        Task.objects.create( title = title, description = description, due = due)
        return redirect('todo_index')       
      else:
        print(f"\nform.errors: {form.errors.items()}\n")
        pass
        # print(f"###### INVALID FORM")           
    # render the create form:
    elif request.method == 'GET':      
      form = CreateUpdateTaskForm()    

    template_file = 'todo_app/add.html'

    context = {
        'form': form,
        'app_name': app_name,         
        'page_name': 'Add Task'       
    }

    return render(request, template_file, context)


# /todos/update/id => update a task with given id
def update(request, id,  **kwargs):
  task = Task.objects.get(id=id)

  if request.method == "POST":    
    form = CreateUpdateTaskForm(request.POST)
    
    if form.is_valid():       
      title = form.cleaned_data['title']
      description = form.cleaned_data['description']
      due = form.cleaned_data['due']

      Task.objects.filter(id=id).update( title = title, description = description, due = due)

      return redirect('todo_index')    
  else: 
    # render the update form on Get method:    
    form = CreateUpdateTaskForm(model_to_dict(task))    


  template_file = 'todo_app/update.html'

  context = {
      'task': task,
      'form': form,
      'app_name': app_name,         
      'page_name': 'Update Task'       
  }

  return render(request, template_file, context)

# /todos/delete/id => delete a task with given id
def delete(request, id, **kwargs):          

    Task.objects.filter(id=id).delete()

    return redirect('todo_index')

# /todos/complete/id => complete a task with given id
def complete(request, id): 
    task = Task.objects.get(id=id)

    task.completed = not task.completed;

    task.save()

    return redirect('todo_index')

