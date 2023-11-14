from django.db import models

# Create your models here.
class Hostel(models.Model):
    name=models.CharField( max_length=50)
    hostel_address=models.CharField( max_length=50)
    created_at=models.DateField( auto_now=True, auto_now_add=False)
    modifide_at=models.DateTimeField( auto_now=False, auto_now_add=True)
   
class Room(models.Model):
      
    room_number=models.CharField( max_length=50)
    number_of_seats=models.IntegerField()
    attached_washroom=models.BooleanField()
    remarks=models.TextField()
    created_at=models.DateField( auto_now=False, auto_now_add=True)
    modifide_at=models.DateTimeField( auto_now=True, auto_now_add=False)
    