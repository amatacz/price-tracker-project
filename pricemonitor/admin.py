from django.contrib import admin
from pricemonitor.models.userprofile import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


admin.site.register(UserProfile)

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False


# class AccountsUserAdmin(AuthUserAdmin):
#     inlines = [UserProfileInline]


# admin.site.unregister(User)
# admin.site.register(User, AccountsUserAdmin)

