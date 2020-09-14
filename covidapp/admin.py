from django.contrib import admin
from .models import Departments
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class DepartmentsAdmin(LeafletGeoAdmin):
    list_display = ("code", "nom")

admin.site.register(Departments, DepartmentsAdmin)