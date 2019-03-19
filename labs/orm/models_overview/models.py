from django.db import models
import datetime

# Users:
#   id: autoincrement
#   name: varchar(max: 45)
#   age: number
#   mail: varchar
#   created_on: timestamp



# TODO: fix You are trying to add the field 'created_on' with 'auto_now_add=True' to users without a default
class Users(models.Model):
  name = models.CharField(max_length=45)  
  age = models.IntegerField(default=0)
  mail = models.CharField(max_length=100,null=True)
  created_on = models.DateTimeField(default=datetime.datetime.now )  


