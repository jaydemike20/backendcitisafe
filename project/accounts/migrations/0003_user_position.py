# Generated by Django 4.2.4 on 2023-08-24 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
