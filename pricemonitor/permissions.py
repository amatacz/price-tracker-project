from django.contrib.auth.mixins import PermissionRequiredMixin


class ModeratorPermissionMixin(PermissionRequiredMixin):

    def has_permission(self):
        return self.request.user.profile.role == 'moderator'

class UserRequestPermissionMixin(PermissionRequiredMixin):
    def has_permission(self):
        return self.request.user.id == self.request.user.id
