from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import os

# models for accounts
# table for profile of rta officer
def profile_pic_upload_path(instance, filename):
    # Construct the upload path dynamically
    return f"profile_pics/{filename}".format(filename=filename)    

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        TREASURER = "TREASURER", 'Treasurer'
        ENFORCER = "ENFORCER", 'Enforcer'

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.ADMIN)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(default='profile_pics/image.png' , upload_to='profile_pics/', null=True, blank=True)

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
    

class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.ADMIN)
    
class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for administrator"    
    
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
    

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'accounts':
        username = os.getenv('DJANGO_ADMIN_USERNAME')
        email = os.getenv('DJANGO_ADMIN_EMAIL')
        password = os.getenv('DJANGO_ADMIN_PASSWORD')

        if not User.objects.filter(username=username).exists():
            # Create the superuser with is_active set to False
            superuser = User.objects.create_superuser(
                username=username, email=email, password=password, role="ADMIN")

            # Activate the superuser
            superuser.is_active = True
            print('Created admin account')
            superuser.save()
