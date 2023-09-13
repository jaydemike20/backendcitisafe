from django.db import models
from drivers.models import Driver

# Create your models here.

# admin
class vehicle_type(models.Model):
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.model
    
class registered_owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=1)
    address = models.CharField(max_length=255)

    def __str__(self):
        # Concatenate the first name, middle initial, and last name
        full_name = f"{self.first_name} {self.middle_initial}. {self.last_name}"
        return full_name
 
    
class vehicle(models.Model):

    # foreign keys
    driverID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle_type_ID = models.ForeignKey(vehicle_type, on_delete=models.CASCADE)
    owner_ID = models.ForeignKey(registered_owner, on_delete=models.CASCADE)

    # other fields
    plate_number = models.CharField(max_length=50, unique=True)
    make = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    vehicle_class = models.CharField(max_length=255)
    body_markings = models.CharField(max_length=100)


    def __str__(self):
        return self.plate_number
    