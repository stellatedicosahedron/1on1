# Generated by Django 4.2 on 2024-04-06 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invites", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invite",
            name="date_sent",
            field=models.DateField(default="2024-04-06"),
        ),
    ]
