from django.db import models

# Create your models here.
class Payments(models.Model):
    tenant=models.ForeignKey("tenants.Tenant", on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    payment_type=models.CharField(max_length=20 , choices=[('Security', 'security'), ('Rent', 'rent'),('Mess', 'mess'), ('utility', 'utility')])
    remarks=models.TextField()
    payment_date=models.DateField( auto_now=False, auto_now_add=False) 
    valid_from=models.DateField( auto_now=False, auto_now_add=False)
    valid_untill=models.DateField( auto_now=False, auto_now_add=False)
    created_at=models.DateField( auto_now=False, auto_now_add=False)
    updated_at=models.DateTimeField( auto_now=False, auto_now_add=False)  