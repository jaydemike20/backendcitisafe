from django.contrib import admin
from ticket.models import penalty, violation, traffic_violation, ticket
# Register your models here.


admin.site.register(penalty)
admin.site.register(violation)
admin.site.register(traffic_violation)
admin.site.register(ticket)