# Generated by Django 3.2 on 2021-05-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_react_app', '0006_auto_20210505_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='action_taken',
        ),
        migrations.AddField(
            model_name='lead',
            name='Action_taken',
            field=models.TextField(blank=True, default='NO ISSUE', max_length=300, null=True, verbose_name='Action taken'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='message_body',
            field=models.TextField(default='NO ISSUE', null=True, verbose_name='Message body'),
        ),
    ]