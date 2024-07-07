from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Rental
from .serializers import RentalSerializer
from bikes.models import Bike
from .tasks import calculate_rental_cost


class RentalCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        active_rental = Rental.objects.filter(user=request.user,
                                              end_time__isnull=True).first()
        if active_rental:
            return Response({'error': ('You already have an active rental.'
                                       ' Please return the bike first.')},
                            status=status.HTTP_400_BAD_REQUEST)

        bike = Bike.objects.filter(status='available').first()
        if not bike:
            return Response({'error': 'No available bikes'},
                            status=status.HTTP_400_BAD_REQUEST)

        rental = Rental.objects.create(user=request.user, bike=bike)
        bike.status = 'rented'
        bike.save()

        return Response(RentalSerializer(rental).data)


class RentalEndView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        rental = Rental.objects.filter(user=request.user,
                                       end_time__isnull=True).first()
        if not rental:
            return Response({'error': 'No active rental found'},
                            status=status.HTTP_400_BAD_REQUEST)

        rental.end_time = timezone.now()
        rental.save()
        bike = rental.bike
        bike.status = 'available'
        bike.save()

        calculate_rental_cost.delay(rental.id)

        return Response(RentalSerializer(rental).data)


class RentalHistoryView(generics.ListAPIView):
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rental.objects.filter(user=self.request.user)
