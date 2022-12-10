import datetime

from django.db import models
from importlib import import_module

from django.core.exceptions import ValidationError
 
# creating a validator function
def validate_url(value):
    domains = ['.pl', '.com', '.de', '.it']
    if any(domain in value for domain in domains):
        return value
    else:
        raise ValidationError("Podaj prawidłowy link")
 

class Service(models.Model):
    STATUSES = (
        ("p", "Oczekuje"),
        ("r", "Odrzucone"),
        ("a", "Zaakceptowane")
    )

    host = models.CharField(max_length=255, verbose_name="Adres URL", validators=[validate_url])
    service_name = models.CharField(max_length=30, verbose_name="Nazwa techniczna sklepu")
    verbose_name = models.CharField(max_length=30, verbose_name="Nazwa sklepu")
    status = models.CharField(max_length=1, choices=STATUSES, default="p")
    published_data = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.verbose_name

