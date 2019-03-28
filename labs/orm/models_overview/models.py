from django.db import models
import datetime

# User:
#   id: primary key, autoincrement
#   name: varchar(max: 45, not null)
#   age: number(not null)
#   mail: varchar
#   created_on: timestamp

class Users(models.Model):
  name = models.CharField(max_length=45)  
  age = models.IntegerField(default=0)
  mail = models.CharField(max_length=100,null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True) 

  def __str__(self):
    return self.name

class Task(models.Model):
  title = models.CharField('Title', max_length=100)
  description = models.TextField('Description', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title
  


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
