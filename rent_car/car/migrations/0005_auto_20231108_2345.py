# Generated by Django 3.2.21 on 2023-11-09 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20231108_2325'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Testemonial',
        ),
    ]
