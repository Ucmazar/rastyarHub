from django.db import models
from accounts.models import BaseProfile, CustomUser

class ManagerProfile(BaseProfile):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='manager_profile')

    def __str__(self):
        return f"Manager Profile of {self.user.username}"
