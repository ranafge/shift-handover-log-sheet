# Generated by Django 3.2 on 2021-05-05 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoreAlarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_name', models.CharField(max_length=500)),
                ('alarm_type', models.CharField(max_length=50)),
                ('alarm_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DatacomAlarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_name', models.CharField(max_length=500)),
                ('alarm_type', models.CharField(max_length=50)),
                ('alarm_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PowerAlarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_name', models.CharField(max_length=500)),
                ('alarm_type', models.CharField(max_length=50)),
                ('alarm_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reporting_Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('designation', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionAlarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_name', models.CharField(max_length=500)),
                ('alarm_type', models.CharField(max_length=50)),
                ('alarm_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')], default='morning', max_length=15)),
                ('Fault_description', models.TextField(blank=True, default='No issue', max_length=250, null=True, verbose_name='Fault Description')),
                ('action_taken', models.TextField(blank=True, default='NO ISSUE', max_length=300, null=True, verbose_name='Action Taken')),
                ('message_body', models.TextField(default='NO ISSUE', null=True, verbose_name='Message Body')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('have_sms_send', models.BooleanField(default=False)),
                ('Corealarm', models.ForeignKey(blank=True, default='No alarm', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corealarm', to='drf_react_app.corealarm')),
                ('Datacomalarm', models.ForeignKey(blank=True, default='No alarm', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datacomalarm', to='drf_react_app.datacomalarm')),
                ('Poweralarm', models.ForeignKey(blank=True, default='No alarm', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poweralarm', to='drf_react_app.poweralarm')),
                ('Transmissionalarm', models.ForeignKey(blank=True, default='No alarm', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissionalarm', to='drf_react_app.transmissionalarm')),
                ('dept', models.ManyToManyField(blank=True, default='core', null=True, to='drf_react_app.Dept')),
                ('engineer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drf_react_app.engineer')),
            ],
            options={
                'ordering': ['-created_at', 'shift'],
            },
        ),
    ]
