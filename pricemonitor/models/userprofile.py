import datetime

from django.db import models
from pricemonitor.models.serviceproduct import ServiceProduct
from importlib import import_module


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=30, choices=(('regular', 'Użytkownik'), ('moderator', 'Moderator')), default='moderator')


class UserProductAssignment(models.Model):
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name="assignments")
    serviceproduct = models.ForeignKey("ServiceProduct", on_delete=models.CASCADE)
    