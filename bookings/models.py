from django.db import models
from hostels.models import models

# Create your models here.

class SeatBooking(models.Model):
      
    room_number=models.CharField( max_length=50)
    seat=models.ForeignKey("hostels.Seat", on_delete=models.CASCADE)
    remarks=models.TextField() 
    created_at=models.DateField( auto_now=False, auto_now_add=True)
    modifide_at=models.DateTimeField( auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.room_number
    