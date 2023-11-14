from django.contrib import admin

# Register your models here.

from .models import Hostel,Room
admin.site.register(Hostel)
admin.site.register(Room)