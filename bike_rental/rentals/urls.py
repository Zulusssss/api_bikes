from django.urls import path
from .views import RentalCreateView, RentalEndView, RentalHistoryView

urlpatterns = [
    path('rent/', RentalCreateView.as_view(), name='rent-bike'),
    path('return/', RentalEndView.as_view(), name='return-bike'),
    path('history/', RentalHistoryView.as_view(), name='rental-history'),
]
