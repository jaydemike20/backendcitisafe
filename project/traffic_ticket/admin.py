from django.contrib import admin
from traffic_ticket.models import traffic_violation, penalty, violation, ticket

# Register your models here.

admin.site.register(traffic_violation)
admin.site.register(penalty)
admin.site.register(violation)
admin.site.register(ticket)