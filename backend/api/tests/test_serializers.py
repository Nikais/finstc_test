from django.test import TestCase

from api.models import Car
from api.serializers import CarSerializer


class CarSerializerTestCase(TestCase):
    def test_ok(self):
        car_1 = Car.objects.create(name='Aventador', price=10_000_000)
        car_2 = Car.objects.create(name='M5', price=6_000_000)

        serializer_data = CarSerializer([car_1, car_2], many=True).data
        expected_data = [
            {
                'id': car_1.id,
                'name': 'Aventador',
                'price': '10000000.00',
            },
            {
                'id': car_2.id,
                'name': 'M5',
                'price': '6000000.00',
            },
        ]

        self.assertEqual(expected_data, serializer_data)