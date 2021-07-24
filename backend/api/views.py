__all__ = ['BrandViewSet', 'CarViewSet', 'DealerViewSet']

from rest_framework import viewsets

from .models import *
from .serializers import *


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class DealerViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = Dealer.objects.all()
