from django.contrib import admin

# Register your models here.

from .models import Tenant,TenantDocument
admin.site.register(Tenant)
admin.site.register(TenantDocument)
