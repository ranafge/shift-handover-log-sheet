
from django.contrib.auth.models import User
from rest_framework import serializers
from . import models

class UserSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ('id',)

class EngineerSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.Engineer
        exclude = ('id',)

class ReportingBossSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reporting_Boss
        exclude = ('id',)

# class AlarmSrializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Alarm
#         exclude = ('id',)


class DeptSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dept
        exclude = ('id',)


class PowerAlarmSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.PowerAlarm
        exclude = ('id',)

class CoreAlarmSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.CoreAlarm
        exclude = ('id',)

class DatacomAlarmSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.DatacomAlarm
        exclude = ('id',)

class TransmissionAlarmSrializer(serializers.ModelSerializer):
    class Meta:
        model = models.TransmissionAlarm
        exclude = ('id',)

class reactAppSrializer(serializers.ModelSerializer):
    core = CoreAlarmSrializer(many=True, read_only=True)

    class Meta:
        model = models.Lead
        fields = ('core',"shift",'engineer_name',
        "Fault_description","Power_alarm","Datacom_alarm","Core_alarm","Transmission_alarm", "Action_taken",'message_body',"created_at",'have_sms_send')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # rep["dept"] = DeptSrializer(instance.dept.all(), many=True).data
        rep["engineer_name"] = EngineerSrializer(instance.engineer_name).data
        rep["Poweralarm"] = PowerAlarmSrializer(instance.Power_alarm).data
        rep["Corealarm"] = CoreAlarmSrializer(instance.Core_alarm).data
        rep["Datacomalarm"] = DatacomAlarmSrializer(instance.Datacom_alarm).data
        rep["Transmissionalarm"] = TransmissionAlarmSrializer(instance.Transmission_alarm).data
        # rep["escalation_to"] = ReportingBossSrializer(instance.escalation_to.all(), many=True).data
        return rep





# class CategorySerializer(serializers.ModelSerializer):
#     items = serializers.RelatedField(read_only=True)
#     class Meta:
#         model = models.Category
#         fields = ("name",'items',)

#     def to_representation(self, instance):
#         self.fields['items'] = ItemSrializer(read_only=True)
#         return super(CategorySerializer, self).to_representation(instance)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('username', 'password',)
