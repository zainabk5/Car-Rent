# Generated by Django 3.2.21 on 2023-11-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_booking_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_email', models.EmailField(max_length=254)),
                ('admin_phone', models.CharField(max_length=100)),
                ('admin_password', models.CharField(max_length=100)),
            ],
        ),
    ]
