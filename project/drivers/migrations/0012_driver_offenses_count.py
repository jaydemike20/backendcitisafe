# Generated by Django 4.2.6 on 2023-11-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0011_alter_driver_classification'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='offenses_count',
            field=models.IntegerField(default=0),
        ),
    ]
