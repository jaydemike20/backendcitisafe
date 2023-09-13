from django.urls import path, include
from vehicles.views import VehicleListCreateAPIView, VehicleRetrieveUpdateDestroyAPIView, VehicleTypeListCreateAPIView, VehicleTypeRetrieveUpdateDestroyAPIView, OwnerRetrieveUpdateDestroyAPIView, OwnerListCreateAPIView
from django.conf.urls.static import static

urlpatterns = [
    path('register/', VehicleListCreateAPIView.as_view(), name="vehicle-list" ),
    path('register/<int:pk>/', VehicleRetrieveUpdateDestroyAPIView.as_view(), name="vehicle-details" ),
    path('type/', VehicleTypeListCreateAPIView.as_view(), name="vehicle-type-list" ),
    path('type/<int:pk>/', VehicleTypeRetrieveUpdateDestroyAPIView.as_view(), name="vehicle-type-details" ),  
    path('owner/', OwnerListCreateAPIView.as_view(), name="owner-list" ),
    path('owner/<int:pk>/', OwnerRetrieveUpdateDestroyAPIView.as_view(), name="owner-details" ),      
]


