from django.contrib.auth.mixins import PermissionRequiredMixin


<<<<<<< HEAD
class ModeratorPermisionMixin(PermissionRequiredMixin):
=======
class UserPermisionMixin(PermissionRequiredMixin):
>>>>>>> 83c5cfa6f4e0dd156aa2811706d5d49ab811c8c4

    def has_permission(self):
        return self.request.user.profile.role == 'moderator'

<<<<<<< HEAD
=======

>>>>>>> 83c5cfa6f4e0dd156aa2811706d5d49ab811c8c4
class UserRequestPermisionMixin(PermissionRequiredMixin):

    def has_permission(self):
        return self.object.user == self.request.user