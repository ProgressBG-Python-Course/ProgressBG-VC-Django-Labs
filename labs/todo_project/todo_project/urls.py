from django.contrib import admin
from django.urls import path,include


urlpatterns = [	  
  path('todos/', include('todo_app.urls')),
  path('demos/', include('demos.urls')),  
  path('admin/', admin.site.urls),
]