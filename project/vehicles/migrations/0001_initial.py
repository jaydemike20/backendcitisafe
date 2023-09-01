# Generated by Django 4.2.4 on 2023-09-01 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=50, unique=True)),
                ('make', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=50)),
                ('vehicle_class', models.CharField(max_length=255)),
                ('body_markings', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_initial', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('driverID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver')),
                ('vehicle_type_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle_type')),
            ],
        ),
    ]
