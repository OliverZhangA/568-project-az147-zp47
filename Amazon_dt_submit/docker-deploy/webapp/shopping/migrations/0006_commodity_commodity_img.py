# Generated by Django 4.0.1 on 2022-04-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_commodity_commodity_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='commodity_img',
            field=models.CharField(default='/static/img/sample.jpg', max_length=100),
        ),
    ]
