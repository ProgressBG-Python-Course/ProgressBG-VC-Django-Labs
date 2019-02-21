from django.urls import path


from . import views


urlpatterns = [
	# http://127.0.0.1:8000/todos/
	path('', views.index),

	# http://127.0.0.1:8000/todos/list
    path('list/', views.list),

    # http://127.0.0.1:8000/todos/table
    path('table/', views.table),
]