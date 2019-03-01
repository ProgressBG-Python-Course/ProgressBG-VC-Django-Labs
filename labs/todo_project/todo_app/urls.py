from django.urls import path


from . import views


urlpatterns = [
	# 127.0.0.1:8000/todoss
	path('', views.index),

	# http://127.0.0.1:8000/todos/list
  path('list/', views.list),

  # http://127.0.0.1:8000/todos/table
  path('table/', views.table),

  # http://127.0.0.1:8000/todos/delete/2018 
  path('delete/<int:id>', views.delete),

]