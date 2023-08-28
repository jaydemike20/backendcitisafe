from django.urls import path, include
from drivers.views import ClassificationListCreateAPIView, ClassificationRetrieveUpdateDestroyAPIView, DriverListCreateAPIView, DriverRetrieveUpdateDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', DriverListCreateAPIView.as_view(), name="driver-list" ),
    path('register/<int:pk>/', DriverRetrieveUpdateDestroyAPIView.as_view(), name="driver-details" ),
    path('classification/', ClassificationListCreateAPIView.as_view(), name="classification-list" ),
    path('classification/<int:pk>/', ClassificationRetrieveUpdateDestroyAPIView.as_view(), name="classification-details" ),    
]


