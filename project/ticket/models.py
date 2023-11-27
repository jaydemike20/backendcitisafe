import json
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer


from drivers.models import Driver
from vehicles.models import vehicle
from django.contrib.auth import get_user_model
import datetime
from django.utils import timezone as timez

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
    violations = models.ForeignKey(traffic_violation, on_delete=models.CASCADE)
    vehicle = models.ForeignKey('vehicles.vehicle', on_delete=models.CASCADE, related_name='driver_tickets')

    TICKET_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PAID", "Paid"),
        ("OVERDUE", "Overdue"),
        ("DROPPED", "Dropped"),
    ]
    ticket_status = models.CharField(max_length=10, choices=TICKET_STATUS_CHOICES, default="Pending")

    place_violation = models.CharField(max_length=255)
    date_issued = models.DateTimeField(auto_now_add=True)
    signature = models.ImageField(upload_to="signature/", null=True, blank=True)
    # Link the ticket's driver to the vehicle

    # custom primarykey
    def generate_mfrta_tct_no():
        current_year = datetime.datetime.now().year
        last_ticket = ticket.objects.filter(MFRTA_TCT_NO__startswith=str(current_year)).order_by('-MFRTA_TCT_NO').first()

        if last_ticket:
            last_tct_no = last_ticket.MFRTA_TCT_NO
            last_counter = int(str(last_tct_no)[-4:])
            new_counter = last_counter + 1
        else:
            new_counter = 1

        new_tct_no = int(f"{current_year}{new_counter:04d}")
        return new_tct_no

    MFRTA_TCT_NO = models.BigIntegerField(primary_key=True, default=generate_mfrta_tct_no)


    @staticmethod
    def calculate_penalty_amount(violations):
        total_penalty_amount = 0

        # Iterate over each violation associated with the ticket
        for violation in violations.violation_id.all():
            # Add the penalty amount for each violation
            total_penalty_amount += violation.penalty_ID.amount

        return total_penalty_amount
        
    
    def save(self, *args, **kwargs):
        # Check if the driver has a valid license number
        if self.driver_ID and self.driver_ID.license_number:
            # Check if the ticket is being created (not updating)
            is_new_ticket = self._state.adding  # This attribute indicates whether the instance is being saved to the database for the first time

            if is_new_ticket:
                # Increment the offenses_count for the driver associated with this ticket
                self.driver_ID.offenses_count += 1
                self.driver_ID.save()

        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.MFRTA_TCT_NO)

# Add this signal receiver at the end of your models.py
@receiver(post_save, sender=ticket)
def send_ticket_notification(sender, instance, update_fields, **kwargs):
    # Get the channel layer
    channel_layer = get_channel_layer()

    # Send a message to the "broadcast" group
    async def send_notification():
        message = json.dumps({'type': 'ticket.notification', 'message': f'There has been an update of the Records table!: {instance.MFRTA_TCT_NO}'})
        await channel_layer.group_send('broadcast', {'type': 'send_notification', 'message': message})

    # Run the function in the event loop
    from asgiref.sync import async_to_sync
    async_to_sync(send_notification)()

    # If the ticket status is updated, send a status update notification
    if update_fields and 'ticket_status' in update_fields:
        ticket_status = getattr(instance, 'ticket_status', None)
        if ticket_status:
            async def send_status_update():
                status_message = json.dumps({'type': 'ticket.status_update', 'message': f'Ticket {instance.MFRTA_TCT_NO} status updated to {ticket_status}'})
                await channel_layer.group_send('broadcast', {'type': 'send_notification', 'message': status_message})

            # Run the function in the event loop
            async_to_sync(send_status_update)()
