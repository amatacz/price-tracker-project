import datetime

from django.db import models
from pricemonitor.models.serviceproduct import ServiceProduct
from importlib import import_module
from django.contrib.auth.models import User, UserManager

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=30, choices=(('regular', 'Użytkownik'), ('moderator', 'Moderator')), default='regular')
    avatar = models.ImageField(default='default.jpg', upload_to='static/img/profile_images/', null=True)
    bio = models.TextField(null=True)

    objects = UserManager()

    def __str__(self):
        return self.user.username
        

class UserProductAssignment(models.Model):
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name="assignments")
    serviceproduct = models.ForeignKey("ServiceProduct", on_delete=models.CASCADE)
    