# Generated by Django 4.2.4 on 2023-10-02 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_remove_vehicle_vehicle_type_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registered_owner',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='registered_owner',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='registered_owner',
            name='middle_initial',
        ),
    ]
