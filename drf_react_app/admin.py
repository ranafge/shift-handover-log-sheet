from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Lead)
# admin.site.register(models.Alarm)
# admin.site.register(models.Dept)
admin.site.register(models.Engineer)
admin.site.register(models.PowerAlarm)
admin.site.register(models.CoreAlarm)
admin.site.register(models.TransmissionAlarm)
admin.site.register(models.DatacomAlarm)
# admin.site.register(models.Reporting_Boss)
