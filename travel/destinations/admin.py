from django.contrib import admin
from .models import Continent, Destination

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("city",)}
    list_filter = ("country",)
    list_display = ("city", "country")


admin.site.register(Destination, CityAdmin)
admin.site.register(Continent)