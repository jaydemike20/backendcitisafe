from django.db import models
from django.contrib.auth import get_user_model

# model sa imong user
User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userRole = models.CharField(max_length=20)
    middleName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=13)
    