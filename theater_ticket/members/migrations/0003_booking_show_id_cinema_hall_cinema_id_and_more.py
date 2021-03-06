# Generated by Django 4.0.4 on 2022-06-19 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_booking_cinema_cinema_hall_cinema_seat_movie_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='show_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.show'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cinema_hall',
            name='cinema_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.cinema'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cinema_seat',
            name='cinema_hall_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.cinema_hall'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='booking_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.booking'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show',
            name='cinema_hall_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.cinema_hall'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show',
            name='movie_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show_seat',
            name='booking_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.booking'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show_seat',
            name='cinema_seat_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.cinema_seat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show_seat',
            name='show_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.show'),
            preserve_default=False,
        ),
    ]
