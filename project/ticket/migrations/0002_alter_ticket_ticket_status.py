# Generated by Django 5.0 on 2023-12-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('OVERDUE', 'Overdue'), ('DROPPED', 'Dropped'), ('COMMUNITY SERVICE', 'Community Service')], default='Pending', max_length=50),
        ),
    ]