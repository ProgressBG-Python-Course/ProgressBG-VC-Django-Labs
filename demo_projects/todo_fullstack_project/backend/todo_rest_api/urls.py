from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url('tasks', views.task_list),
    url('task/<int:id>', views.task_detail),
]