import datetime

from django.db import models
from importlib import import_module

class Service(models.Model):
    host = models.URLField(max_length=255)
    service_name = models.CharField(max_length=30, verbose_name="Nazwa techniczna serwisu")
    verbose_name = models.CharField(max_length=30, verbose_name="Nazwa serwisu")
    published_data = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)