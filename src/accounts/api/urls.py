from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from src.accounts.api.views import register

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', register),
    path('token/refresh/', TokenRefreshView.as_view()),
]
