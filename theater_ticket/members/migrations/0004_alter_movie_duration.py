# Generated by Django 4.0.4 on 2022-06-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_booking_show_id_cinema_hall_cinema_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.TimeField(),
        ),
    ]