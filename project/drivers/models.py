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

    CLASSIFICATION_CHOICES = [
        ('P', 'Professional'),
        ('NP', 'Non-Professional'),
        ('SP', 'Student-Permit'),
        ('O', 'Other')
    ]
    
    officer = models.ForeignKey(User, on_delete=models.CASCADE)
    classification = models.CharField(max_length=2, choices=CLASSIFICATION_CHOICES, null=True, blank=True)
    license_number = models.CharField(max_length=50, null=True, blank=True)
    # full name
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)
    offenses_count = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if self.license_number is None or self.license_number == '':
            self.license_number = 'No License'
            self.classification = None  # or set a default classification for cases without a license
        elif self.license_number != 'No License' and self.classification is None:
            raise ValueError("Classification cannot be null when license_number is not null.")

        # Check for uniqueness of license_number, but skip if it's 'No License' or an empty string
        if self.license_number not in ['No License', '']:
            duplicate_drivers = Driver.objects.filter(license_number=self.license_number).exclude(id=self.id)
            if duplicate_drivers.exists():
                raise ValidationError("License number must be unique.")

        super().save(*args, **kwargs)


    def calculate_penalty_amount(self):
        total_penalty_amount = 0

        # Iterate over each violation associated with the ticket
        for violation in self.violations.violation_id.all():
            # Add the penalty amount for each violation
            total_penalty_amount += violation.penalty_ID.amount

        return total_penalty_amount        
    