from django.urls import path
from models_overview import views


# http://127.0.0.1:8000/models_overview/
urlpatterns = [
    path('', views.index, name='index'),
]
