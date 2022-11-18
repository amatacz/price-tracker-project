import datetime

from django.db import models
from importlib import import_module

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    verbose_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.verbose_name}"