from rest_framework import serializers
from .models import Reservation
from app.trips.models import Trip
from app.customers.models import Cliente

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'