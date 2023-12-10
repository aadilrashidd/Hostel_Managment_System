from django.contrib import admin

# Register your models here.

from .models import Hostel,Room,Seat
admin.site.register(Hostel)
admin.site.register(Room)
admin.site.register(Seat)