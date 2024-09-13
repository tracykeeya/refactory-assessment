from django.urls import path
from .views import flight_booking_view  # Import the view

urlpatterns = [
    path('flight-booking/',flight_booking_view, name='flight_booking'),
]
