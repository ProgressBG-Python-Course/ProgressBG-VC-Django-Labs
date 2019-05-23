from django.conf.urls import url 
from . import views 
 
urlpatterns = [ 
    url(r'^tasks/$', views.task_list),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail),
    url(r'^tasks/completed/(?P<completed>[0-9]+)/$', views.task_list_completed),
]