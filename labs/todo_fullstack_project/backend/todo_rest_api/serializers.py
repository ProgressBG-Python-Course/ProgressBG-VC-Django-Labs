from rest_framework import serializers
from todo_rest_api.models import Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ('title','description','image','due','completed')