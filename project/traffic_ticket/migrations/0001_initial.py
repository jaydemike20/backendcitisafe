# Generated by Django 4.2.4 on 2023-09-01 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import traffic_ticket.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='violation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation_type', models.CharField(max_length=255)),
                ('penalty_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic_ticket.penalty')),
            ],
        ),
        migrations.CreateModel(
            name='traffic_violation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('violation_id', models.ManyToManyField(to='traffic_ticket.violation')),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('ticket_status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('DISMISSED', 'Dismissed')], default='Pending', max_length=10)),
                ('place_violation', models.CharField(max_length=255)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('signature', models.ImageField(blank=True, null=True, upload_to='signature/')),
                ('MFRTA_TCT_NO', models.BigIntegerField(default=traffic_ticket.models.ticket.generate_mfrta_tct_no, primary_key=True, serialize=False)),
                ('driver_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver')),
                ('traffic_violation_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic_ticket.traffic_violation')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_tickets', to='vehicles.vehicle')),
            ],
        ),
    ]