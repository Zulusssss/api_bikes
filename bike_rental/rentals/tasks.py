from celery import shared_task
from .models import Rental


@shared_task
def calculate_rental_cost(rental_id):
    rental = Rental.objects.get(id=rental_id)
    duration = (rental.end_time - rental.start_time).total_seconds() / 60
    rental.cost = duration * 10
    rental.save()
