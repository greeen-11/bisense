from django.urls import path
from .views import ping

urlpatterns = [
    path('ping/', ping, name='ping'),  # Endpoint to check if the API is working
]