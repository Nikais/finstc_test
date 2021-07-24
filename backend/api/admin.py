from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )


@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = ('__str__', 'brand', 'year', )
    list_filter = ('year', 'brand', )
    search_fields = ('name', 'brand__name', 'year', )
    readonly_fields = ('date_created', 'date_edited')


@admin.register(Dealer)
class DealerAdmin(ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)

