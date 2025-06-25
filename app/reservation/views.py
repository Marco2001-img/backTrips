from rest_framework import viewsets
from .models import Reservation
from app.trips.models import Trip
from app.customers.models import Cliente
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
