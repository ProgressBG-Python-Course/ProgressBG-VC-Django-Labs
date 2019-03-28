from django.db import models
import datetime

# User:
#   id: primary key, autoincrement
#   name: varchar(max: 45, not null)
#   age: number(not null)
#   mail: varchar
#   created_at: timestamp
#   updated_at: timestamp
# more on auto_now_add: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.DateField
class User(models.Model):
  name = models.CharField(max_length=45)  
  age = models.IntegerField(default=0)
  mail = models.CharField(max_length=100,null=True)
  # created_on = models.DateTimeField(default=datetime.datetime.now )  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 



# One to Many relation:
# One User can have Many tasks 
class Task(models.Model):
  title = models.CharField('Title', max_length=100)
  description = models.TextField('Description', null=True)
  user = models.ForeignKey(User,on_delete=models.PROTECT)
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)   

  # We allway want to have a meaningful string representation of the model instance, so we define __str__() method
  def __str__(self):
    return self.title


# Many to Many relation:
# A product can be sold in many sotres. A store can sell many products
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    products = models.ManyToManyField(Product,blank=True)
