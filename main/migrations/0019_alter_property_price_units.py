# Generated by Django 3.2.6 on 2021-09-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210921_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price_units',
            field=models.CharField(choices=[('K', 'K'), ('M', 'M')], default='', max_length=10),
        ),
    ]
