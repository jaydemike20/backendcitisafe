from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Classification(models.Model):
    class_type = models.CharField(max_length=5)
    
class Agency(models.Model):
    agency_code = models.CharField(max_length=255)

class Driver(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agency = models.OneToOneField(Agency, on_delete=models.CASCADE)
    classification = models.OneToOneField(Classification, on_delete=models.CASCADE)

    license_number = models.CharField(max_length=15, null=False, blank=False)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    expiration_date = models.DateField()
    blood_type = models.CharField(max_length=3)
    eyes_color = models.CharField(max_length=20)
    dl_codes = models.CharField(max_length=100)
    condition = models.CharField(max_length=10)
