from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Store, StoreContent

# Register your models here.

@admin.register(Store)
class StoreAdmin(GISModelAdmin):
    list_display = ('name', 'address', 'store_type')
    search_fields = ('name',)

admin.site.register(StoreContent)