from django.db import models
from drivers.models import Driver
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

# admin
class vehicle_type(models.Model):
    model = models.CharField(max_length=255)
    year_model = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            self.year_model = int(self.model)
        except ValueError:
            self.year_model = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.model
    
# enforcer
class registered_owner(models.Model):
    name = models.CharField(max_length=100)  
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_initial}. {self.last_name}" 
    
class vehicle(models.Model):

    officer = models.ForeignKey(User, on_delete=models.CASCADE)
    # foreign keys
    driverID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    # vehicle_type_ID = models.ForeignKey(vehicle_type, on_delete=models.CASCADE)
    owner_ID = models.ForeignKey(registered_owner, on_delete=models.CASCADE)

    # other fields
    plate_number = models.CharField(max_length=50)
    make = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    vehicle_class = models.CharField(max_length=255)
    body_markings = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=255)

    def __str__(self):
        return self.plate_number
    