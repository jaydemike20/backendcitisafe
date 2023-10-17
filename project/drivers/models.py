from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError

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
    middle_initial = models.CharField(max_length=1, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.license_number is None:
            self.license_number = 'No License'
            
        if self.license_number is not None:
            if self.classification is None:
                raise ValueError("Classification cannot be null when license_number is not null.")

            # Check for uniqueness of license_number
            if Driver.objects.filter(license_number=self.license_number).exclude(id=self.id).exists():
                raise ValidationError("License number must be unique.")
                
        super().save(*args, **kwargs)
    