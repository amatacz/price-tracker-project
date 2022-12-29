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

class Product(models.Model):

    STATUSES = (
        ("p", "Oczekuje"),
        ("r", "Odrzucone"),
        ("a", "Zaakceptowane")
    )

    product_name = models.CharField(max_length=255, verbose_name="Nazwa techniczna", null=True)
    verbose_name = models.CharField(max_length=255, verbose_name="Nazwa produktu", null=True)
    status = models.CharField(max_length=1, choices=STATUSES, default="p")
    product_URL = models.CharField(max_length=255, verbose_name="Link do produktu", validators=[validate_url], default="brak adresu")

    def __str__(self):
        return self.verbose_name
