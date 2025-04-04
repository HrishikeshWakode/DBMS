
from django.db import models

from django.db import models

class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    ROLE_CHOICES = [
        ('blood bank staff', 'Blood Bank Staff'),
        ('hospital staff', 'Hospital Staff'),
        ('admin', 'Admin'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=10)
    units_available = models.IntegerField()

    def __str__(self):
        return f"{self.blood_group} - {self.units_available}"

