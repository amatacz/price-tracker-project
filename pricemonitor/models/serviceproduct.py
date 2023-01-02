import datetime

from django.db import models
from importlib import import_module
from pricemonitor.models.product import Product
from pricemonitor.models.service import Service

from django.core.exceptions import ValidationError
 
# creating a validator function
def validate_url(value):
    domains = ['.pl', '.com', '.de', '.it']
    if any(domain in value for domain in domains):
        return value
    else:
        raise ValidationError("Podaj prawidłowy link")
        

class ServiceProductManager(models.Manager):

    def get_from_data(self, service_name, product_name, status):
        return self.get(product__name=product_name, service__name=service_name, status=status)


class ServiceProduct(models.Model):
    STATUSES = (
        ("p", "Oczekuje"),
        ("r", "Odrzucone"),
        ("a", "Zaakceptowane")
    )

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name="products")
    product_url = models.CharField(max_length=255, default="no address", validators=[validate_url])
    status = models.CharField(max_length=1, choices=STATUSES, default="p")


    def __str__(self):
        return f"{self.product.verbose_name} z {self.service.service_name}"

    def validate_product_url_and_host(self):
        if self.service.service_name not in self.product_url:
            raise ValidationError("Link produktu nie pochodzi z właściwego sklepu")


class ServiceProductItemManager(models.Manager):
    def register_from_data(self, data, service_product):
        if data.get(service_product):
            self.create(
                service_product=service_product,
                date=data[service_product].get("date"),
                price=data[service_product].get("price")
            )


class ServiceProductItem(models.Model):
    service_product = models.ForeignKey("ServiceProduct", related_name="items", on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    object = ServiceProductItemManager()


class ServiceProductDataRequestManager(models.Manager):

    def register_tasks(self):
        service_products = ServiceProduct.objects.all()
        for sp in service_products:
            self.create(
                service_product=sp,
            )


class ServiceProductDataRequest(models.Model):
    service_product = models.ForeignKey("ServiceProduct", related_name="requests", on_delete=models.CASCADE)
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(null=True)
    status = models.CharField(max_length=12, default='p', choices=(('e', 'Błąd'), ('p', 'Oczekuje'), ('d', 'Wykonano'), ('r', 'W trakcie')))
    error_message = models.TextField(default='')

    objects = ServiceProductDataRequestManager()

    def get_data(self):
        self.status = 'r'
        self.save()
        #parser = import_module(f'pricemonitor.backend.{self.service_product.service.service_name}.parser')
        parser = import_module('pricemonitor.backend.ceneo.parser')

        # czy poniżej url powinien równać się wynikowi wyszukiwania na ceneo -> w takim razie stworzyć przykładowy ServiceProduct
        # i wtedy przypisywać na pdst. service_product.service.service_url
        # zrobic dodatkowe pole w SP z linkiem ceneo
        parser_obj = parser.Parser(
            url=self.service_product.product_url,
        )
        try:
            response = parser_obj.process()
        except Exception as e:
            self.status = 'e'
            self.error_message = str(repr(e))
        else:
            ServiceProductItem.object.register_from_data(response, self.service_product)
            self.status = 'd'
        self.end_datetime = datetime.datetime.now()
        self.save()