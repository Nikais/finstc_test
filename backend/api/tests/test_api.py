from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Car, Dealer
from ..serializers import CarSerializer


class CarApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.car_1 = Car.objects.create(brand='BMW', name='M5', year=2019)
        self.car_2 = Car.objects.create(brand='Mercedes-Benz', name='E200', year=2021)
        self.car_3 = Car.objects.create(brand='BMW', name='X6', year=2017)

    def test_get(self):
        url = reverse('car-list')
        print(url)
        response = self.client.get(url)
        serializer = CarSerializer([self.car_1, self.car_2, self.car_3], many=True)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_get_filter(self):
        url = reverse('car-list')
        response = self.client.get(url, data={'price': 6_000_000})
        serializer = CarSerializer([self.m5, self.e200], many=True)
        self.assertEqual(serializer.data, response.data)

    def test_get_search(self):
        url = reverse('car-list')
        response = self.client.get(url, data={'search': '200'})
        serializer = CarSerializer([self.e200], many=True)
        self.assertEqual(serializer.data, response.data)