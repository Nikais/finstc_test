__all__ = ['Brand', 'Car', 'Dealer']

from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Dealer(models.Model):
    name = models.CharField(max_length=64)
    brands = models.ManyToManyField(Brand, related_name='dealers')

    def __str__(self):
        return self.name


class Car(models.Model):
    vin = models.CharField(max_length=17, validators=[MinLengthValidator(17)], unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    mark = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, null=True, blank=True)
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.brand} {self.mark}'



