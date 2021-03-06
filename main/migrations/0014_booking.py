# Generated by Django 3.2.6 on 2021-09-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_property_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_posted', '-id'),
            },
        ),
    ]
