from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ticket.views import penaltyListCreateAPIView, penaltyRetrieveUpdateDestroyAPIView, violationListCreateAPIView, violationRetrieveUpdateDestroyAPIView, trafficviolationListCreateAPIView, trafficviolationRetrieveUpdateDestroyAPIView, ticketListCreateAPIView, ticketRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('register/', ticketListCreateAPIView.as_view(), name="ticket-list" ),
    path('register/<int:pk>/', ticketRetrieveUpdateDestroyAPIView.as_view(), name="ticket-details" ),
    path('penalty/', penaltyListCreateAPIView.as_view(), name="penalty-list" ),
    path('penalty/<int:pk>/', penaltyRetrieveUpdateDestroyAPIView.as_view(), name="penalty-details" ),   
    path('violation/', violationListCreateAPIView.as_view(), name="violation-list" ),
    path('violation/<int:pk>/', violationRetrieveUpdateDestroyAPIView.as_view(), name="violation-details" ),
    path('trafficviolation/', trafficviolationListCreateAPIView.as_view(), name="trafficviolation-list" ),
    path('trafficviolation/<int:pk>/', trafficviolationRetrieveUpdateDestroyAPIView.as_view(), name="trafficviolation-details" ),         
]