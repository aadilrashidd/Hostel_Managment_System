from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    user_type=models.CharField(max_length=20 , choices=[('owner', 'owner'), ('tenent', 'tenent')])
    email=models.EmailField( max_length=254)
    phone=models.CharField( max_length=13)
    address=models.CharField( max_length=50)
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    date_of_birth=models.DateField( auto_now=False, auto_now_add=False)
    date_joined=models.DateField( auto_now=False, auto_now_add=False)
    last_login=models.DateTimeField( auto_now=False, auto_now_add=False)