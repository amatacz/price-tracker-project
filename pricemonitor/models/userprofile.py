import datetime

from django.db import models
from importlib import import_module


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=30, choices=(('regular', 'Użytkownik'), ('moderator', 'Moderator')), default='regular')
