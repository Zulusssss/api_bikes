from django.db import models
from django.contrib.auth import get_user_model
from bikes.models import Bike

User = get_user_model()


class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                               blank=True)
