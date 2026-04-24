from django.urls import path
from .views import fuel_route

urlpatterns = [
    path('fuel-route/', fuel_route),
]