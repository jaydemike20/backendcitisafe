from django.db import models
from drivers.models import Driver
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

# Create your models here.
class penalty(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    PENALTY_STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]
    status = models.CharField(max_length=10, choices=PENALTY_STATUS_CHOICES, default="Active")    
    date = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.description
    

class violation(models.Model):
    penalty_ID = models.ForeignKey(penalty, on_delete=models.CASCADE)
    violation_type = models.CharField(max_length=255)

    def __str__(self):
        return self.violation_type
    
class traffic_violation(models.Model):

    violation_id = models.ManyToManyField(violation)

    def __str__(self):
        return str(self.id) 
    

class ticket(models.Model):

    driver_ID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)

    TICKET_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("DISMISSED", "Dismissed"),
    ]
    ticket_status = models.CharField(max_length=10, choices=TICKET_STATUS_CHOICES, default="Pending")

    place_violation = models.CharField(max_length=255)
    date_issued = models.DateTimeField(auto_now_add=True, auto_now=False)
    signature = models.ImageField(upload_to="signature/", null=True, blank=True)
    # Link the ticket's driver to the vehicle
    vehicle = models.ForeignKey('vehicles.vehicle', on_delete=models.CASCADE, related_name='driver_tickets', blank=True, null=True)

    # custom primarykey

    def generate_mfrta_tct_no():
        current_year = datetime.datetime.now().year
        last_ticket = ticket.objects.order_by('-MFRTA_TCT_NO').first()

        if last_ticket:
            last_tct_no = last_ticket.MFRTA_TCT_NO
            last_year = int(str(last_tct_no)[:6])

            if last_year == current_year:
                counter = int(str(last_tct_no)[6:]) + 1
            else:
                counter = 1
        else:
            counter = 1

        return int(f"{current_year}{counter:06d}")

    MFRTA_TCT_NO = models.BigIntegerField(primary_key=True, default=generate_mfrta_tct_no)

    def __str__(self):
        return self.MFRTA_TCT_NO