from django.db import models

# Create your models here.
class Hostel(models.Model):
    name=models.CharField( max_length=50)
    hostel_address=models.CharField( max_length=50)
    created_at=models.DateField( auto_now=True, auto_now_add=False)
    modifide_at=models.DateTimeField( auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.name
   
class Room(models.Model):
      
    room_number=models.CharField( max_length=50)
    attached_washroom=models.BooleanField()
    remarks=models.TextField()
    created_at=models.DateField( auto_now=False, auto_now_add=True)
    modifide_at=models.DateTimeField( auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.room_number
class Seat(models.Model):
    seat_number=models.IntegerField
    room=models.ForeignKey("hostels.Room", on_delete=models.CASCADE)
    def __str__(self):
        return self.room
    
    