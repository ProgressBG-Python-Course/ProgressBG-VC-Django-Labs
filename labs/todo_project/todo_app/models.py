from django.db import models
from django.utils import timezone
from datetime import datetime


def days_from_now_1():  
  return timezone.now() + timezone.timedelta(days=n)

# Create your models here.
class Task(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField('Title', max_length=100)
  description = models.TextField('Description', null=True)
  created = models.DateTimeField(auto_now_add=True)
  due = models.DateTimeField('due', default=days_from_now_1)
  completed = models.BooleanField(default=False)
  

  def __str__(self):
    return f"{self.title} - {self.description}"

