import imp
from django.contrib import admin

from .models import Pantry, Location, Item
# Register your models here.

admin.site.register(Pantry)
admin.site.register(Location)
admin.site.register(Item)