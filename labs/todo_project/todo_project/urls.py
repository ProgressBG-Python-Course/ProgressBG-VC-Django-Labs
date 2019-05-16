from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [	  
  path('auth/', include('user_auth.urls')),
  path('todos/', include('todo_app.urls')),
  path('html_forms/', include('html_forms_demo.urls')),  
  path('django_forms_labs/', include('django_forms_labs.urls')),  
  path('django_forms_demo/', include('django_forms_demo.urls')),  
  path('demos/', include('demos.urls')),  
  path('admin/', admin.site.urls),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)