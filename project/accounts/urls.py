from django.urls import path, include
from accounts.views import ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('users/profile/', ProfileListCreateAPIView.as_view(), name="profile-list" ),
    path('users/profile/<str:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-details" )
]
