from django.urls import path, re_path

from . import views

urlpatterns = [
    path('list', views.list, name='list'),
    path('table', views.table, name='table'),
    path('task/<int:id>', views.task, name='task'),

    # http://127.0.0.1:8000/demos/user/ivan
    # http://127.0.0.1:8000/demos/user/ivan/ivanov
    # => "Hello ivan"

    # http://127.0.0.1:8000/demos/user/1
    # => 'Hello ivan'

   

    # http://127.0.0.1:8000/demos/user/ivan/ivanov
    
    # http://127.0.0.1:8000/demos/user/ivan
    # http://127.0.0.1:8000/demos/user/1
    
    # TODO: give examples with capturing groups with pure Python regex
    re_path('user/(?:([A-Za-z]+)|(\d+))$', views.user),   
    
]
				