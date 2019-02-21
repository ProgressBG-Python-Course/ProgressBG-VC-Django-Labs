from django.contrib import admin
from django.urls import path,include


urlpatterns = [	

    path('', include('todo_app.urls')),
    path('todos/', include('todo_app.urls')),
    path('demos/', include('demos.urls')),
    path('admin/', admin.site.urls),
]