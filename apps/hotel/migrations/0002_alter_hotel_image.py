# Generated by Django 4.2.8 on 2024-03-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(upload_to='hotel-images/', verbose_name='View of the hotel'),
        ),
    ]
