from django.test import TestCase

from api.models import *


class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(name='Toyota')

    def setUp(self) -> None:
        self.brand = Brand.objects.get(id=1)

    def test_name_label(self):
        field_label = self.brand._meta.get_field('name').verbose_name
        self.assertEqual('name', field_label)

    def test_name_max_length(self):
        max_length = self.brand._meta.get_field('name').max_length
        self.assertEqual(64, max_length)

    def test_object_name(self):
        expected_object_name = self.brand.name
        self.assertEquals(expected_object_name, str(self.brand))


class DealerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Dealer.objects.create(name='Toyota MAXIMUM')

    def setUp(self) -> None:
        self.dealer = Dealer.objects.get(id=1)

    def test_name_label(self):
        field_label = self.dealer._meta.get_field('name').verbose_name
        self.assertEqual('name', field_label)

    def test_name_max_length(self):
        max_length = self.dealer._meta.get_field('name').max_length
        self.assertEqual(64, max_length)
