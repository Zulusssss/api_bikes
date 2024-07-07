from rest_framework import viewsets, permissions
from .models import Bike
from .serializers import BikeSerializer


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = [permissions.AllowAny]
