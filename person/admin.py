from django.contrib import admin
from .models import Supplier,Distributor,Vaccinator,Vaccine,Patient,Appointment

admin.site.register(Supplier)
admin.site.register(Distributor)
admin.site.register(Vaccinator)
admin.site.register(Vaccine)
admin.site.register(Patient)
admin.site.register(Appointment)
