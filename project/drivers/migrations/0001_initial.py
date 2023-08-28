# Generated by Django 4.2.4 on 2023-08-28 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('contact_number', models.CharField(max_length=50)),
                ('nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('expiration_date', models.DateField()),
                ('blood_type', models.CharField(blank=True, max_length=3, null=True)),
                ('eyes_color', models.CharField(blank=True, max_length=20, null=True)),
                ('agency_code', models.CharField(max_length=255)),
                ('dl_codes', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=10)),
                ('classification', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='drivers.classification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
