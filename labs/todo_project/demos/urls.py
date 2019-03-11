from django.urls import path, re_path

from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('table', views.table, name='table'),    
    path('task/<int:id>', views.task, name='task'),
    path('form', views.form, name='form'),        
    path('form_process', views.form_process, name='form_process'),        
]
				