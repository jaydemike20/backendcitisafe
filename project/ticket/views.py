from datetime import datetime, timedelta, timezone
from django.http import JsonResponse
from django.db.models import Count
from django.shortcuts import render
from ticket.serializers import penaltySerializers, violationSerializer, traffic_violationSerializer, ticketSerializer
from ticket.models import penalty, violation, traffic_violation, ticket
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.permissions import EnforcerPermission, AdminPermission, TreasurerPermission
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import ticket
import datetime as dt
import calendar
import pandas as pd

from django.http import JsonResponse

def traffic_violation_count(request):
    # Get all traffic violations
    all_traffic_violations = traffic_violation.objects.all()

    # Create a dictionary to store the counts
    violation_counts = {}

    # Loop through each traffic violation
    for violation_instance in all_traffic_violations:
        # Loop through each violation associated with the traffic violation
        for v in violation_instance.violation_id.all():
            violation_type = v.violation_type

            # Update or set the count in the dictionary
            violation_counts[violation_type] = violation_counts.get(violation_type, 0) + 1

    # Convert the counts dictionary to the desired format
    counts_list = [{"name": violation_type, "value": count} for violation_type, count in violation_counts.items()]

    # Return the counts as JSON response
    return JsonResponse(counts_list, safe=False)

def get_monthly_data(request):
    # Get the current month and year
    current_month = dt.datetime.now().month
    current_year = dt.datetime.now().year

    # Get the first and last day of the current month
    _, last_day = calendar.monthrange(current_year, current_month)
    first_day = dt.date(current_year, current_month, 1)
    last_day = dt.date(current_year, current_month, last_day)

    weekly_data = []
    daily_data = []

    # Iterate over the weeks in the current month
    for week_start in pd.date_range(first_day, last_day, freq='W-MON'):
        week_end = week_start + pd.DateOffset(days=6)

        # Calculate the daily data for each day in the week
        for day in pd.date_range(week_start, week_end):
            # Perform your calculations or queries to get the daily data
            # Example: Get the count of tickets issued on the current day
            daily_count = ticket.objects.filter(date_issued__date=day).count()

            # Append the daily data to the list
            daily_data.append((day.strftime('%A'), daily_count))

        # Append the weekly data to the list
        weekly_data.append((week_start.strftime('%B %d'), daily_data))
        daily_data = []

    context = {
        'weekly_data': weekly_data
    }

    return JsonResponse({'weekly_data': weekly_data})

# dashboard purposes
def ticket_data(request):
    # Get the current year
    current_year = datetime.now().year

    # Get the number of tickets by month
    tickets_by_month = ticket.objects.filter(date_issued__year=current_year).values('date_issued__month').annotate(count=Count('MFRTA_TCT_NO'))

    # Get the number of tickets by week
    tickets_by_week = ticket.objects.filter(date_issued__year=current_year).values('date_issued__week').annotate(count=Count('MFRTA_TCT_NO'))

    # Get the number of tickets by day
    tickets_by_day = ticket.objects.filter(date_issued__year=current_year).values('date_issued__day').annotate(count=Count('MFRTA_TCT_NO'))

    # Create a dictionary to store the ticket data
    ticket_data = {
        'by_month': {},
        'by_week': {},
        'by_day': {},
        'total': ticket.objects.count(),
    }

    # Populate the ticket data dictionaries
    for entry in tickets_by_month:
        month = entry['date_issued__month']
        count = entry['count']
        month_name = datetime(datetime.now().year, month, 1).strftime("%B")
        ticket_data['by_month'][month_name] = count

    for entry in tickets_by_week:
        week = entry['date_issued__week']
        count = entry['count']
        week_start_date = datetime.strptime(f"{datetime.now().year}-W{week}-1", "%Y-W%W-%w")
        week_start_day = week_start_date.strftime("%A")
        month_name = week_start_date.strftime("%B")
        week_key = f"by_week OF {month_name}"
        if week_key not in ticket_data['by_week']:
            ticket_data['by_week'][week_key] = {}
        ticket_data['by_week'][week_key][week] = {
            'start_day': week_start_day,
            'count': count
        }

    for entry in tickets_by_day:
        day = entry['date_issued__day']
        count = entry['count']
        date = datetime(datetime.now().year, datetime.now().month, day)
        day_of_week = date.strftime("%A")
        ticket_data['by_day'][day] = {
            'day_of_week': day_of_week,
            'count': count
        }


    # # Group tickets by month
    # for ticket_month in tickets_by_month:
    #     month_name = datetime(current_year, ticket_month['date_issued__month'], 1).strftime('%B')
    #     ticket_data['by_month'][month_name] = ticket_month['count']

    # # Group tickets by week
    # for ticket_week in tickets_by_week:
    #     week_number = ticket_week['date_issued__week']
    #     if week_number not in ticket_data['by_week']:
    #         ticket_data['by_week'][week_number] = {}
    #     ticket_data['by_week'][week_number] = ticket_week['count']

    # # Group tickets by day
    # for ticket_day in tickets_by_day:
    #     day_number = ticket_day['date_issued__day']
    #     ticket_data['by_day'][day_number] = ticket_day['count']


    return JsonResponse(ticket_data)



def ticket_daily(request):
    # Get the current year, month, and day
    today = datetime.now()
    current_year = today.year
    current_month = today.month
    current_day = today.day

    # Get the start and end timestamps for the current day
    start_of_day = datetime(current_year, current_month, current_day, 0, 0, 0)
    end_of_day = datetime(current_year, current_month, current_day, 23, 59, 59)

    # Get the count of tickets for the current day
    tickets_count = ticket.objects.filter(date_issued__range=[start_of_day, end_of_day]).count()

    # Return the ticket count as JSON response
    return JsonResponse({"total_tickets": tickets_count})

# Create your views here.

class penaltyListCreateAPIView(ListCreateAPIView):
    serializer_class = penaltySerializers
    queryset = penalty.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]


class penaltyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = penaltySerializers
    queryset = penalty.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]
    


class violationListCreateAPIView(ListCreateAPIView):
    serializer_class = violationSerializer
    queryset = violation.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]


class violationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = violationSerializer
    queryset = violation.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]



class trafficviolationListCreateAPIView(ListCreateAPIView):
    serializer_class = traffic_violationSerializer
    queryset = traffic_violation.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]


class trafficviolationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = traffic_violationSerializer
    queryset = traffic_violation.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]


class ticketListCreateAPIView(ListCreateAPIView):
    serializer_class = ticketSerializer
    queryset = ticket.objects.all()
    permission_classes = [IsAuthenticated & (EnforcerPermission)]

    # def get_queryset(self):
    #     # Filter traffic tickets based on the logged-in officer
    #     return ticket.objects.filter(user_ID=self.request.user)

    def perform_create(self, serializer):
        # Set the user as the authenticated user when creating a driver instance
        serializer.save(user_ID=self.request.user)


class ticketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ticketSerializer
    queryset = ticket.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission | EnforcerPermission | TreasurerPermission)]
