from django.db import models

# Create your models here.
class Task(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField('Title', max_length=100)
  description = models.TextField('Description')
  created = models.DateTimeField(auto_now_add=True)
  due = models.DateTimeField('due date')
  end = models.DateTimeField('end date')

  def __str__(self):
    return f"{self.title} - {self.description}"

