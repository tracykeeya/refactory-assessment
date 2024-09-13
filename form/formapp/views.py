from django.shortcuts import render, redirect
from .forms import FlightBookingForm
from django.contrib import messages

# Create your views here.
def flight_booking_view(request):
    if request.method == 'POST':
        form = FlightBookingForm(request.POST, request.FILES)  # Include request.FILES for file upload
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted successfully')
            return redirect('/')
        else:
            messages.error(request, 'Form is not valid')
    else:
        form = FlightBookingForm()
    return render(request, 'formapp/flight_booking.html', {'form': form})
