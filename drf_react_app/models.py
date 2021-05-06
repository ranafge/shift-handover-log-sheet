from django.db import models
from django.contrib.auth.models import User

class Dept(models.Model):
    dept = models.CharField(max_length=30)

    def __str__(self):
        return self.dept


# class Alarm(models.Model):
#     alarm_name = models.CharField(max_length=500)
#     alarm_type = models.CharField(max_length=50)
#     alarm_description = models.TextField()

#     def __str__(self):
#         return f' {self.alarm_name} ({self.alarm_description})'



class PowerAlarm(models.Model):
    alarm_name = models.CharField(max_length=500,default='No Alarm', null=True)
    # alarm_type = models.CharField(max_length=50, blank=True)
    alarm_description = models.TextField(blank=True,default='No description')

    def __str__(self):
        return f' {self.alarm_name} ({self.alarm_description})'

class CoreAlarm(models.Model):
    alarm_name = models.CharField(max_length=500,default='No Alarm', null=True)
    # alarm_type = models.CharField(max_length=50, blank=True)
    alarm_description = models.TextField(blank=True, default='No description')

    def __str__(self):
        return f' {self.alarm_name} ({self.alarm_description})'


class TransmissionAlarm(models.Model):
    alarm_name = models.CharField(max_length=500,default='No Alarm', null=True)
    # alarm_type = models.CharField(max_length=50, blank=True)
    alarm_description = models.TextField(blank=True,default='No description')

    def __str__(self):
        return f' {self.alarm_name} ({self.alarm_description})'


class DatacomAlarm(models.Model):
    alarm_name = models.CharField(max_length=500, default='No Alarm', null=True)
    # alarm_type = models.CharField(max_length=50, blank=True)
    alarm_description = models.TextField(blank=True, default='No description')

    def __str__(self):
        return f' {self.alarm_name} ({self.alarm_description})'

    

class Engineer(models.Model):
    name = models.CharField(max_length=500)
    # designation = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name


class Reporting_Boss(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Lead(models.Model):
    shift = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
       )
    dept = (
        ('core', 'CORE'),
        ('power', 'POWER'),
        ('transmission', 'TRANSMISSION'),
        ('datacom', 'DATACOM'),
       )

    shift = models.CharField(max_length=15,choices=shift, default='morning')
    engineer_name = models.ForeignKey(Engineer, on_delete=models.CASCADE)
    Fault_description = models.TextField('Fault description',max_length=250, blank=True, null=True, default='No issue')
    message_body = models.TextField('Message body', null=True, default='NO ISSUE')
    Power_alarm = models.ForeignKey(PowerAlarm,  null=True, blank=True, related_name='poweralarm', on_delete=models.CASCADE)
    Datacom_alarm = models.ForeignKey(DatacomAlarm,  null=True, blank=True, related_name='datacomalarm', on_delete=models.CASCADE)
    Core_alarm = models.ForeignKey(CoreAlarm,  null=True, blank=True, related_name='corealarm', on_delete=models.CASCADE)
    Transmission_alarm = models.ForeignKey(TransmissionAlarm,  null=True, blank=True, related_name='transmissionalarm', on_delete=models.CASCADE)
    # dept = models.ManyToManyField(Dept, default='core', null=True, blank=True)
    Action_taken = models.TextField('Action taken',max_length=300, null=True, blank=True, default='NO ISSUE')
    created_at = models.DateTimeField(auto_now_add=True)
    # escalation_to = models.ManyToManyField(Reporting_Boss, blank=True,null=True, default='NO')
    have_sms_send =  models.BooleanField(default=False)

    def __str__(self):
        return f'Engineer:  {self.engineer_name}'

    class Meta:
        ordering = ['-created_at','shift', 'message_body', 'Fault_description']
