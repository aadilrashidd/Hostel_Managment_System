from django.db import models

# Create your models here.
room=models.ForeignKey("hostels.Room", on_delete=models.CASCADE)
lease_start=models.DateField( auto_now=False, auto_now_add=False)
lease_end=models.DateField( auto_now=False, auto_now_add=False)
move_in=models.DateField( auto_now=False, auto_now_add=False)
move_out=models.DateField( auto_now=False, auto_now_add=False)
security_deposit=models.PositiveIntegerField()
monthly_rent=models.PositiveIntegerField()
created_at=models.DateField( auto_now=False, auto_now_add=False)
updated_at=models.TimeField( auto_now=False, auto_now_add=False)
