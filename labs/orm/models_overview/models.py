from django.db import models
import datetime

# Users:
#   id: autoincrement
#   name: varchar(max: 45)
#   age: number
#   mail: varchar
#   created_on: timestamp

# DONE: 
#   problem: You are trying to add the field 'created_on' with 'auto_now_add=True' to users without a default...
#   explain: the Model was already created, and we have set 'auto_now_add=True' on Alter..., 
#   fix1: when DB is empty: delete all migrations and the Users Model from db and then run:
#   fix2: to prevent data loss: use fixtures
class Users(models.Model):
  name = models.CharField(max_length=45)  
  age = models.IntegerField(default=0)
  mail = models.CharField(max_length=100,null=True)
  # created_on = models.DateTimeField(default=datetime.datetime.now )  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 
# more on auto_now_add: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.DateField

class Task(models.Model):
  title = models.CharField('Title', max_length=100)
  description = models.TextField('Description', null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  completed = models.BooleanField(default=False)
  

