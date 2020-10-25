from django.contrib import admin
from . models import District, Division, Upazila, Cadre

# Register your models here.
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upazila)
admin.site.register(Cadre)