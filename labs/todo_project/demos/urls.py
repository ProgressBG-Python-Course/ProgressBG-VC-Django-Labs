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

   


    # TODO: upload as HW - to match only 3 types of URLS
    # http://127.0.0.1:8000/demos/user/ivan/ivanov
    
    # http://127.0.0.1:8000/demos/user/ivan
    # http://127.0.0.1:8000/demos/user/1
    
    # TODO: give examples with capturing groups with pure Python regex
    re_path('user/((?P<user_name>[A-Za-z]+)|(?P<id>\d+))$', views.user),       
    
]
				