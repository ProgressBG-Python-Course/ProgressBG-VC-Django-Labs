from django.db import models
import datetime

# Users:
#   id: autoincrement
#   name: varchar(max: 45)
#   age: number
#   mail: varchar
#   created_on: timestamp

class Users(models.Model):
  name = models.CharField(max_length=45)  
  age = models.IntegerField(default=0)
  mail = models.CharField(max_length=100,null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 
# more on auto_now_add: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.DateField

class Task(models.Model):
  title = models.CharField('Title', max_length=100)
  description = models.TextField('Description', null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title
  

