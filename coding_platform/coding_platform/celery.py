# coding_platform/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coding_platform.settings")

app = Celery("coding_platform")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
