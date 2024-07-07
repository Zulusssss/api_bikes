from django.db import models


class Bike(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('rented', 'Rented'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='available')
