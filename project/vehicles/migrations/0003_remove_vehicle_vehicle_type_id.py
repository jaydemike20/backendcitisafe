# Generated by Django 4.2.4 on 2023-10-02 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehicle_vehicle_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='vehicle_type_ID',
        ),
    ]
