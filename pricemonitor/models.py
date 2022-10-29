import datetime

from django.db import models
from importlib import import_module


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    #role 


class Service(models.Model):
    host = models.URLField(max_length=255)
    service_name = models.CharField(max_length=30, verbose_name="Nazwa techniczna serwisu")
    verbose_name = models.CharField(max_length=30, verbose_name="Nazwa serwisu")
    published_data = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    verbose_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.verbose_name}"


class ServiceProductManager(models.Manager):

    def get_from_data(self, service_name, product_name):
        return self.get(product__name=product_name, service__name=service_name)


class ServiceProduct(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name="products")
    product_url = models.URLField(max_length=255, default="no address")

    objects = ServiceProductManager()

    def __str__(self):
        return f"{self.product.verbose_name}"


class ServiceProductItemManager(models.Manager):

    def register_from_data(self, data):
        self.create(
            service_product=ServiceProduct.objects.get_from_data(data.get("service_name"), data.get("product_name")),
            date=data.get("date"),
            price=data.get("price")
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

    def get_data(self):
        self.status = 'r'
        self.save()
        parser = import_module(f'pricetracker.pricemonitor.backend.{self.service_product.service.service_name}.parser')
        parser_obj = parser.Parser(
            url=self.service_product.product_url,
            product_name=self.service_product.product_name
        )
        try:
            response = parser_obj.get_data()
        except Exception as e:
            self.status = 'e'
            self.error_message = str(repr(e))
        else:
            ServiceProductItem.object.register_from_data(response)
            self.status = "d"
        self.end_datetime = datetime.datetime.now()
        self.save()


class ProductUserRequest(models.Model):
    STATUSES = (
        ("p", "Oczekuje"),
        ("r", "Odrzucone"),
        ("a", "Zaakceptowane")
    )
    user = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    verbose_name = models.CharField(max_length=255, verbose_name="Nazwa produktu")
    product_url = models.URLField(max_length=255, verbose_name="Link do produktu")
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUSES, default="p")