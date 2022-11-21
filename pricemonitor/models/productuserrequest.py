import datetime
from pricemonitor.models.userprofile import UserProfile
from django.db import models
from importlib import import_module

class ProductUserRequest(models.Model):
    STATUSES = (
        ("p", "Oczekuje"),
        ("r", "Odrzucone"),
        ("a", "Zaakceptowane")
    )
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    verbose_name = models.CharField(max_length=255, verbose_name="Nazwa produktu")
    product_url = models.URLField(max_length=255, verbose_name="Link do produktu")
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES, default="p")