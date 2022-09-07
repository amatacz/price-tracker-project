from django.db import models


class Service(models.Model):
    host = models.URLField(max_length=255)
    name = models.CharField(max_length=30)
    verbose_name = models.CharField(max_length=30)
    published_data = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    verbose_name = models.CharField(max_length=255)
    product_url = models.URLField(max_length=255, default="no address")


class ServiceProduct(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)

