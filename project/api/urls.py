from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('drivers/', include('drivers.urls')),
    path('vehicles/', include('vehicles.urls'))
]