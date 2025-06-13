import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alxtravelapp.settings')

app = Celery('alx_travel_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
