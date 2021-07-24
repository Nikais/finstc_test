__all__ = ['DealerSerializer', 'CarSerializer', 'BrandSerializer']

from rest_framework import serializers

from .models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'brand', 'mark', 'year', 'price', 'dealer')


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'
