from pricemonitor.models.userprofile import UserProfile
from django.db import models


from django.core.exceptions import ValidationError
 
# creating a validator function
def validate_url(value):
    domains = ['.pl', '.com', '.de', '.it']
    if any(domain in value for domain in domains):
        return value
    else:
        raise ValidationError("Podaj prawidłowy link")

class ProductUserRequest(models.Model):
    STATUSES = (
        ("p", "Oczekuje"),
        ("r", "Odrzucone"),
        ("a", "Zaakceptowane")
    )
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, verbose_name="Nazwa techniczna")
    verbose_name = models.CharField(max_length=255, verbose_name="Nazwa produktu")
    product_url = models.CharField(max_length=255, verbose_name="Link do produktu", default="no address", validators=[validate_url])
    #service = models.ForeignKey("Service", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES, default="p")

    def __str__(self):
        return self.verbose_name

        #NIEUŻYWANE
