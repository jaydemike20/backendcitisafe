from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ticket.views import penaltyListCreateAPIView, penaltyRetrieveUpdateDestroyAPIView, violationListCreateAPIView, violationRetrieveUpdateDestroyAPIView, trafficviolationListCreateAPIView, trafficviolationRetrieveUpdateDestroyAPIView, ticketListCreateAPIView, ticketRetrieveUpdateDestroyAPIView
from ticket.views import ticket_data, ticket_daily, get_monthly_data, traffic_violation_count

urlpatterns = [
    path('register/', ticketListCreateAPIView.as_view(), name="ticket-list" ),
    path('register/<int:pk>/', ticketRetrieveUpdateDestroyAPIView.as_view(), name="ticket-details" ),
    path('penalty/', penaltyListCreateAPIView.as_view(), name="penalty-list" ),
    path('penalty/<int:pk>/', penaltyRetrieveUpdateDestroyAPIView.as_view(), name="penalty-details" ),   
    path('violation/', violationListCreateAPIView.as_view(), name="violation-list" ),
    path('violation/<int:pk>/', violationRetrieveUpdateDestroyAPIView.as_view(), name="violation-details" ),
    path('trafficviolation/', trafficviolationListCreateAPIView.as_view(), name="trafficviolation-list" ),
    path('trafficviolation/<int:pk>/', trafficviolationRetrieveUpdateDestroyAPIView.as_view(), name="trafficviolation-details" ),  
    path('ticket-data/', ticket_data, name='ticket_data'),
    path('ticket-daily/', ticket_daily, name='ticket_data'),
    path('monthly-data/', get_monthly_data, name='monthly_data'),
    path('traffic-violation-count/', traffic_violation_count, name='traffic_violation_count'),


]