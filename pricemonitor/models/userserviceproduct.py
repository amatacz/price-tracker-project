import datetime

from django.db import models
from importlib import import_module

from django.contrib.auth.models import User
from pricemonitor.models.serviceproduct import ServiceProduct

class UserServiceProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_product = models.ForeignKey(ServiceProduct, on_delete=models.CASCADE, related_name="followed")

    def get_latest_price(self):
        items = self.service_product.items.all()
        if items:
            return items.latest('date') # to uzyc w template, zeby user widzial cene