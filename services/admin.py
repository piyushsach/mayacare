from django.contrib import admin
from .models import Beneficiary, Service

# Register your models here.
admin.site.register(Beneficiary)
admin.site.register(Service)