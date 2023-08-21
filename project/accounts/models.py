from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# models for accounts

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField("User", on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.user.username + "'s Profile"



class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        TREASURER = "TREASURER", 'Treasurer'
        ENFORCER = "ENFORCER", 'Enforcer'

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.ADMIN)
    middle_name = models.CharField(max_length=50, null=True, blank=True)

class EnforcerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ENFORCER)

class Enforcer(User):
    objects = EnforcerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for enforcer"

class TreasurerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TREASURER)

class Treasurer(User):
    objects = TreasurerManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for treasurer"
    

