# Generated by Django 4.2 on 2024-04-01 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_meeting_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='isInviteeResponseReceived',
            field=models.BooleanField(default=False),
        ),
    ]
