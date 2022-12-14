from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from pricemonitor.models.userprofile import UserProfile
from pricemonitor.models.product import Product
 
 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



