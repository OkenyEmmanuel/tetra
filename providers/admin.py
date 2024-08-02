from django.contrib import admin
from .models import Department, Department_Details, Doctor, ClientAppointment
# Register your models here.
admin.site.register(Department)
admin.site.register(Department_Details)
admin.site.register( Doctor)
admin.site.register(ClientAppointment)
