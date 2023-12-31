# # tasks.py
from celery import shared_task
# from datetime import timedelta
from django.utils import timezone
from .models import ticket
import datetime
# @shared_task
# def update_ticket_status():
#     print("Task started.")
#     overdue_tickets = ticket.objects.filter(ticket_status="PENDING", date_issued__lte=timezone.now()-timedelta(minutes=1))
#     print(f"Found {overdue_tickets.count()} overdue tickets.")
#     overdue_tickets.update(ticket_status="OVERDUE")
#     print("Task completed.")



@shared_task
def update_ticket_status():
    print("Task started.")

    tickets = ticket.objects.filter(ticket_status="PENDING")
    for each in tickets:
        if timezone.now() > each.date_issued + datetime.timedelta(days=3):
            each.ticket_status = "OVERDUE"
            each.save()