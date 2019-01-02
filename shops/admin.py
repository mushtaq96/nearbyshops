from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop
from django.contrib import admin #add this line


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
