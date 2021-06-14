from django.contrib import admin
from .models import Doctor
from .models import Patient
from .models import  Physp


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'designation', 'phone_number')


admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age')


admin.site.register(Patient, PatientAdmin)


class PhyspAdmin(admin.ModelAdmin):
    list_display = ('physp_id', 'physp', 'physp_name')


admin.site.register(Physp, PhyspAdmin)

