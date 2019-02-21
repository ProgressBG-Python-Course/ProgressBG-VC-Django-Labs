from django.urls import path

from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('table', views.table, name='table'),
    path('task/<int:id>', views.task, name='task'),
]
				