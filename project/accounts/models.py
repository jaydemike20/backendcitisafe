from django.db import models
from django.contrib.auth import get_user_model

# model sa imong user
User = get_user_model()

# Create your models here.
class User(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        TREASURER = "TREASURER", 'Treasurer'
        ENFORCER = "ENFORCER", 'Enforcer'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)