from django.db import models
from django.core.exceptions import ValidationError
from datetime import date



#Fields:
#Full name, Gender, Date of Birth, Nationality, Phone Number, Email Address, P.O BOX Number, Emergency phone number,Passport number, Visa Document, Departure City, Destination City.

# Create your models here.
class FlightBooking(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
    full_name = models.CharField(max_length=100, null=True, blank=False)
    gender = models.CharField(max_length=50, null=True, blank=False, choices=GENDER)
    date_of_birth = models.DateField(default=0, null=True, blank=False)
    nationality = models.CharField(max_length=100, null=True, blank=False)
    phone_number = models.PositiveIntegerField(default=0, null=True, blank=False)
    email_address = models.CharField(max_length=255, null=True, blank=False)
    postbox_number = models.CharField(max_length=100)
    emergency_phone_number = models.PositiveIntegerField(default=0,null=True, blank=False)
    passport_number = models.PositiveIntegerField(default=0, null=True, blank=False)
    visa_document = models.FileField()
    departure_city = models.CharField(max_length=255, null=True, blank=False)
    destination_city = models.CharField(max_length=255, null=True, blank=False)

    def _str_(self): 
        return self.full_name
    
    
