from django.db import models
from django.urls import reverse

# Create your models here.

MAINT_TYPES = (
    ('O', 'Oil Change'),
    ('T', 'Tire Rotation'),
    ('B', 'Brake Service')
)

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Maintenance(models.Model):
    date = models.DateField()
    maint_type = models.CharField(
        max_length=1,
        choices=MAINT_TYPES,
        default=MAINT_TYPES[0][0]
        )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_maint_type_display()} on {self.date}"
