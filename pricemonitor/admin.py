from django.contrib import admin
from pricemonitor.models.userprofile import UserProfile
from pricemonitor.models.serviceproduct import ServiceProduct
from pricemonitor.models.product import Product
from pricemonitor.models.service import Service
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(ServiceProduct)
