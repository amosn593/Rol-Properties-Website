# Generated by Django 3.2.6 on 2021-09-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_property_price_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price_units',
            field=models.CharField(choices=[(' ', 'No Units'), ('K', 'K'), ('M', 'M')], max_length=10),
        ),
    ]
