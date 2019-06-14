# development-specific settings
from .default import *

DEBUG = True

ALLOWED_HOSTS = ['192.168.100.2','127.0.0.1']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'OPTIONS': {
      'read_default_file': 
        os.path.join(BASE_DIR, 'todo_rest_project/todo_app_db.cnf'),
    },
  },
}
