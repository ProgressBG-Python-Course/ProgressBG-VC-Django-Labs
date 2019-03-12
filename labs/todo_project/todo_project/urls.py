from django.contrib import admin
from django.urls import path,include


urlpatterns = [	  
  path('todos/', include('todo_app.urls')),
  path('html_forms/', include('html_forms_demo.urls')),  
  path('demos/', include('demos.urls')),  
  path('admin/', admin.site.urls),
]