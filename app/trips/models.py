from django.db import models

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    trip_departure = models.CharField(max_length=100)
    trip_arrival = models.CharField(max_length=100)
    meeting_description = models.TextField()
    trip_arrival_time = models.TimeField()
    trip_departure_time = models.TimeField()
    trip_date = models.DateField()
    trip_price = models.DecimalField(max_digits=10, decimal_places=2)
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.trip_departure} to {self.trip_arrival} on {self.trip_date}"