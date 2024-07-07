from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BikeViewSet

router = DefaultRouter()
router.register(r'bikes', BikeViewSet, basename='bike')

urlpatterns = [
    path('', include(router.urls)),
]
