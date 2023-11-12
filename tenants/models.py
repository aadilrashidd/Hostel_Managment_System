from django.db import models

# Create your models her


class Tenant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=210)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    cnic_number = models.CharField(max_length=13)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    tenant_type = models.CharField(max_length=20 , choices=[('student', 'student'), ('job holder', 'job holder')])


class TenantDocument(models.Model):
    tenent = models.ForeignKey("tenants.tenant", on_delete=models.CASCADE)
    remarks = models.TextField()
    file = models.FileField(upload_to=None, max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)







# we have to pass a list of 2-tuples (x,y) to choices attribute of CharField class
# tenant_type = models.CharField(choices=[('student', 'student), ('job holder', 'job holder')])