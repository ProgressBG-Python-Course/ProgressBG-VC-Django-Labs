from rest_framework import serializers
from todo_app.models import Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'