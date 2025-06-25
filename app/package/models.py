from django.db import models

class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=100)
    package_description = models.TextField()
    package_price = models.DecimalField(max_digits=10, decimal_places=2)
    package_owner = models.CharField(max_length=100)

    def __str__(self):
        return self.package_name