from rest_framework import serializers
from .models import Rental


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'user', 'bike', 'start_time', 'end_time', 'cost']
        read_only_fields = ['user', 'start_time', 'end_time', 'cost']
