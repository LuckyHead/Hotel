# Generated by Django 4.2.8 on 2024-03-27 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateTimeField(auto_now_add=True, verbose_name='Check in date')),
                ('check_out_date', models.DateTimeField(blank=True, verbose_name='Check out date')),
                ('is_paid', models.BooleanField(default=False)),
                ('guest', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Guest')),
                ('room', models.ManyToManyField(to='room.room', verbose_name='Room')),
            ],
            options={
                'verbose_name': 'booking',
                'verbose_name_plural': 'bookings',
            },
        ),
    ]
