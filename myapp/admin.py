from django.contrib import admin

# Register your models here.
from .models import City

admin.site.register(City)


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)
