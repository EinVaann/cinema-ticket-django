from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to = "images/")
    description = models.CharField(max_length=512)
    duration = models.IntegerField()
    released_date = models.DateField()
    genre = models.CharField(max_length=256)
    def __str__(self):
        return self.title

class Cinema(models.Model):
    name = models.CharField(max_length=256)
    total_cinema_halls = models.IntegerField()
    def __str__(self):
        return self.name

class Cinema_Hall(models.Model):
    name = models.CharField(max_length=64)
    total_seats = models.IntegerField()
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Cinema_Seat(models.Model):
    seat_name = models.CharField(max_length=10)
    cinema_hall_id = models.ForeignKey(Cinema_Hall, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.cinema_hall_id)+'-'+self.seat_name

class Show(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    cinema_hall_id = models.ForeignKey(Cinema_Hall, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.movie_id) +':'+str(self.cinema_hall_id)

class Booking(models.Model):
    number_of_seats = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.IntegerField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user_id) + '---' + str(self.show_id)

class Show_Seat(models.Model):
    is_empty = models.BooleanField()
    price = models.IntegerField()
    cinema_seat_id = models.ForeignKey(Cinema_Seat, on_delete=models.CASCADE)
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE,null=True,blank=True)

class Payment(models.Model):
    amount = models.IntegerField()
    timestamp = models.DateTimeField()
    payment_method = models.CharField(max_length=100)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)