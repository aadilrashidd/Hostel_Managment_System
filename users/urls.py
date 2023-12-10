from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from users import views

urlpatterns = [
    path("",views.index,name="index")
    
]