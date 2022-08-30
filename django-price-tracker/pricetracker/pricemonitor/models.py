from django.db import models




class Service(models.Model):
    host = models.URLField(max_length=255)
    name = models.CharField(max_length=30)
    verbose_name = models.CharField(max_length=30)
    published_data = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return 'service/list'


class Product(models.Model):
    name = models.CharField(max_length=255)
    verbose_name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return 'product/list'


class ServiceProduct(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return 'serviceproduct/list'
