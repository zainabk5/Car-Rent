# Generated by Django 3.2.21 on 2023-11-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_auto_20231116_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_image', models.ImageField(upload_to='static/')),
                ('client_name', models.CharField(max_length=100)),
                ('client_des', models.TextField(default='true')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]