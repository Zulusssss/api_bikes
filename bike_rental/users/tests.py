import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    url = reverse('register')
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_login():
    client = APIClient()
    url = reverse('token_obtain_pair')
    User.objects.create_user(username='testuser',
                             email='testuser@example.com',
                             password='testpassword')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 200
    assert 'access' in response.data
