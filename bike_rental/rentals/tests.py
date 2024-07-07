import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from bikes.models import Bike
from .models import Rental
from django.utils import timezone

User = get_user_model()


@pytest.mark.django_db
def test_rent_bike():
    client = APIClient()
    url = reverse('rent-bike')
    user = User.objects.create_user(username='testuser',
                                    email='testuser@example.com',
                                    password='testpassword')
    bike = Bike.objects.create(status='available')
    client.force_authenticate(user=user)

    response = client.post(url, format='json')
    assert response.status_code == 200
    assert Rental.objects.count() == 1
    bike.refresh_from_db()
    assert bike.status == 'rented'

    response = client.post(url, format='json')
    assert response.status_code == 400
    assert response.data['error'] == ('You already have an active rental.'
                                      ' Please return the bike first.')

    rental = Rental.objects.first()
    rental.end_time = timezone.now()
    rental.save()
    bike.status = 'available'
    bike.save()

    response = client.post(url, format='json')
    assert response.status_code == 200
    assert Rental.objects.count() == 2
    bike.refresh_from_db()
    assert bike.status == 'rented'


@pytest.mark.django_db
def test_return_bike():
    client = APIClient()
    url = reverse('return-bike')
    user = User.objects.create_user(username='testuser',
                                    email='testuser@example.com',
                                    password='testpassword')
    bike = Bike.objects.create(status='available')
    rental = Rental.objects.create(user=user, bike=bike)
    client.force_authenticate(user=user)
    response = client.post(url, format='json')
    assert response.status_code == 200
    rental.refresh_from_db()
    assert rental.end_time is not None
    bike.refresh_from_db()
    assert bike.status == 'available'
    assert rental.cost is not None
