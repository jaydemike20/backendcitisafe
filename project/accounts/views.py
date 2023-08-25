from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import permissions

# Create your views here.


class ProfileListCreateAPIView(ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(user=user)
        return queryset

class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        try:
            profile = user.userprofile  # Assuming 'userprofile' is the related name in your model
            return profile
        except UserProfile.DoesNotExist:
            raise Http404("Profile not found for this user.")

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(user=user)
        return queryset