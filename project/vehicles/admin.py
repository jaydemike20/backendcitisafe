from django.contrib import admin
from vehicles.models import vehicle_type, vehicle
# Register your models here.


admin.site.register(vehicle)
admin.site.register(vehicle_type)