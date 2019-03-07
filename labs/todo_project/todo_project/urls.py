from django.contrib import admin
from django.urls import path,include


urlpatterns = [	
  # 127.0.0.1:8000/todos
  path('todos/', include('todo_app.urls')),
  path('demos/', include('demos.urls')),
  path('forms_demo/', include('forms_demo.urls')),
  path('admin/', admin.site.urls),
]