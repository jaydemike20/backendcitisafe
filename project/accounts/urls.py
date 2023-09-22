from django.urls import path, include
from accounts.views import ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('profile/', ProfileListCreateAPIView.as_view(), name="profile-list" ),
    path('profile/me/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-details" ),
]


