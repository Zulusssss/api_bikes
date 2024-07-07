from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
