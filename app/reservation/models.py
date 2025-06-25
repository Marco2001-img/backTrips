from django.db import models

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey('trips.Trip', on_delete=models.CASCADE, related_name='reservations')
    client = models.ForeignKey('customers.Cliente', on_delete=models.CASCADE, related_name='reservations')

    def __str__(self):
        return f"Reservation {self.reservation_id} - Trip {self.trip.trip_id} for {self.client.email}"
