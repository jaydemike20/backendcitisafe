from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Classification(models.Model):
    class_type = models.CharField(max_length=255)

    def __str__(self):
        return self.class_type
    
    
class Driver(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    officer = models.ForeignKey(User, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True, blank=True)
    license_number = models.CharField(max_length=15, null=True, blank=True)
    # full name
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)
    
    # email = models.CharField(max_length=100, null=True, blank=True)
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    # weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # height = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    # expiration_date = models.DateField(null=True, blank=True)
    # blood_type = models.CharField(max_length=3, null=True, blank=True)
    # eyes_color = models.CharField(max_length=20, null=True, blank=True)
    # agency_code = models.CharField(max_length=255, null=True, blank=True)
    # dl_codes = models.CharField(max_length=100, null=True, blank=True)
    # condition = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"