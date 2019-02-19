from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
from ToDoApp.models import Task

# Create your views here.
def index(request):
    latest_tasks = Task.objects.order_by('due')[:5]

    context = {
        'latest_tasks': {}
    }

    template_file = 'ToDoApp/index.html'


    return render(request, template_file, context)
