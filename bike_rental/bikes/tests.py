import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Bike


@pytest.mark.django_db
def test_bike_list():
    client = APIClient()
    url = reverse('bike-list')
    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_bike_by_id():
    client = APIClient()
    bike = Bike.objects.create(status='available')
    url = reverse('bike-detail', kwargs={'pk': bike.id})
    response = client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == bike.id


@pytest.mark.django_db
def test_create_bike():
    client = APIClient()
    url = reverse('bike-list')
    data = {'status': 'available'}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Bike.objects.count() == 1
    assert Bike.objects.get().status == 'available'


@pytest.mark.django_db
def test_update_bike():
    client = APIClient()
    bike = Bike.objects.create(status='available')
    url = reverse('bike-detail', kwargs={'pk': bike.id})
    data = {'status': 'rented'}
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    bike.refresh_from_db()
    assert bike.status == 'rented'


@pytest.mark.django_db
def test_partial_update_bike():
    client = APIClient()
    bike = Bike.objects.create(status='available')
    url = reverse('bike-detail', kwargs={'pk': bike.id})
    data = {'status': 'rented'}
    response = client.patch(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    bike.refresh_from_db()
    assert bike.status == 'rented'


@pytest.mark.django_db
def test_delete_bike():
    client = APIClient()
    bike = Bike.objects.create(status='available')
    url = reverse('bike-detail', kwargs={'pk': bike.id})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Bike.objects.count() == 0
