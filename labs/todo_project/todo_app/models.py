from django.db import models
from django.utils import timezone


def n_days_from_now(n):
    return timezone.now() + timezone.timedelta(days=n)

# Create your models here.
class Task(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField('Title', max_length=100)
  description = models.TextField('Description')
  created = models.DateTimeField(auto_now_add=True)
  due = models.DateTimeField('due', default=n_days_from_now(1))
  completed = models.BooleanField(default=False)
  

  def __str__(self):
    return f"{self.title} - {self.description}"

