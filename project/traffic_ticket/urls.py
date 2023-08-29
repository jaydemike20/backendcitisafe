from django.urls import path, include
from traffic_ticket.views import PenaltyListCreateAPIView, PenaltyRetrieveUpdateDestroyAPIView, ViolationListCreateAPIView, ViolationRetrieveUpdateDestroyAPIView, TrafficViolationListCreateAPIView, TrafficViolationRetrieveUpdateDestroyAPIView, TicketListCreateAPIView, TicketRetrieveUpdateDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', TicketListCreateAPIView.as_view(), name="ticket-list" ),
    path('register/<int:pk>/', TicketRetrieveUpdateDestroyAPIView.as_view(), name="ticket-details" ),
    path('penalty/', PenaltyListCreateAPIView.as_view(), name="penalty-list" ),
    path('penalty/<int:pk>/', PenaltyRetrieveUpdateDestroyAPIView.as_view(), name="penalty-details" ),   
    path('violation/', ViolationListCreateAPIView.as_view(), name="violation-list" ),
    path('violation/<int:pk>/', TicketRetrieveUpdateDestroyAPIView.as_view(), name="violation-details" ),
    path('trafficviolation/', TrafficViolationListCreateAPIView.as_view(), name="trafficviolation-list" ),
    path('trafficviolation/<int:pk>/', TrafficViolationRetrieveUpdateDestroyAPIView.as_view(), name="trafficviolation-details" ),         
]


