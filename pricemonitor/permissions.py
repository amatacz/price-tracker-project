from django.contrib.auth.mixins import PermissionRequiredMixin


class UserPermisionMixin(PermissionRequiredMixin):

    def has_permission(self):
        return self.request.user.profile.role == 'moderator'


class UserRequestPermisionMixin(PermissionRequiredMixin):

    def has_permission(self):
        return self.object.user == self.request.user