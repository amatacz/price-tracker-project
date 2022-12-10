import datetime

from django.db import models
from importlib import import_module

from django.contrib.auth.models import User
from pricemonitor.models.serviceproduct import ServiceProduct

class UserServiceProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_product = models.ForeignKey(ServiceProduct, on_delete=models.CASCADE)
