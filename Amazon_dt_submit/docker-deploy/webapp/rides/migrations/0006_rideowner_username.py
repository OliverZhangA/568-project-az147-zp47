# Generated by Django 4.0.1 on 2022-01-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0005_remove_rideowner_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='rideowner',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
