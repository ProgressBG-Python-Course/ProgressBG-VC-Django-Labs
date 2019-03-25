from django.contrib import admin

# Register your models here.
from .models import Task,User,Product,Store

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Product)
admin.site.register(Store)