import datetime
from os import device_encoding
from tkinter import N 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CinemaForm, CinemaHallForm, MovieForm, ShowForm , BookingForm ,Show_SeatForm
from django.http import HttpResponseRedirect

def home_page(request):
    return render(request, 'ui/home.html', {})

def admin_page(request):
    return render(request,'ui/admin.html',{})
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            print(request.user.id)
            return redirect('home')
        else:
            messages.success(request, ('There Was An Error'))
            return redirect('login')
    else:
        return render(request, 'ui/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('Logout successfully'))
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password= password)
            # add_base_model(username)
            login(request, user)
            messages.success(request, ('Register successfully'))
            return redirect('home')
    else:
        form = UserCreationForm() 
    return render(request, 'ui/register.html', {
        'form':form,
        })

def get_all_cinemas(request):
    cinema_list = Cinema.objects.all()
    return render(request, 'ui/cinema_list.html', {'cinema_list':cinema_list})

def get_cinema(request, pk):
    cinema = Cinema.objects.get(pk=pk)
    cinema_halls = Cinema_Hall.objects.filter(cinema_id = pk)
    return render(request, 'ui/cinema_info.html', {'cinema':cinema, 'cinema_halls':cinema_halls})

def get_all_show(request):
    show_list = Show.objects.all()
    return render(request, 'ui/show_list.html', {'show_list':show_list})

def get_all_booking(request):
    booking_list = Booking.objects.all()
    return render(request, 'ui/booking_list.html', {'booking_list':booking_list})
    
def get_all_show_seat(request):
    show_seat_list = Show_Seat.objects.all()
    return render(request, 'ui/show_seat_list.html', {'show_seat_list':show_seat_list}) 
    
def get_all_movies(request):
    movie_list = Movie.objects.all()
    return render(request, 'ui/movie_list.html', {'movie_list':movie_list})

def home_page_view(request):
    movies = Movie.objects.all()
    if len(movies) > 10:
        movies = movies[:10]
    return render(request, 'ui/home.html', {'movies':movies})

def create_seats(request):
    seats = Cinema_Seat.objects.all()
    seats.delete()
    cinema_halls = Cinema_Hall.objects.all()
    c = 'ABCDEF'
    n = {1,2,3,4,5,6,7,8}
    for cinema_hall in cinema_halls:
        for cc in c:
            for nn in n:
                seat_name = cc + str(nn)
                seat = Cinema_Seat(seat_name=seat_name, cinema_hall_id=cinema_hall)
                seat.save()
    return redirect('/')

def delete_seats(request):
    seats = Cinema_Seat.objects.all()
    seats.delete()
    return redirect('/')

def add_movie(request):
    submitted = False
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_movie?submitted=True')
    else:
        form = MovieForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'ui/add_movie.html', {'form': form , 'submitted':submitted})
def edit_movie(request, movie_id):
    movie = Movie.objects.get(pk =  movie_id)
    form = MovieForm(request.POST or None, instance = movie)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/movie_list')
    return render(request, 'ui/edit_movie.html', {'form': form, 'movie':movie })
def edit_movie(request, movie_id):
    movie = Movie.objects.get(pk =  movie_id)
    form = MovieForm(request.POST or None, instance = movie)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/movie_list')
    return render(request, 'ui/edit_movie.html', {'form': form, 'movie':movie })


def delete_movie(request, movie_id):
    movie = Movie.objects.get(pk =  movie_id).delete()
    print(movie)
    return HttpResponseRedirect('/movie_list')

def add_show(request):
    submitted = False
    if request.method == "POST":
        form1 = ShowForm(request.POST)
        if form1.is_valid():
            form1.save()
            hall_id = form1['cinema_hall_id'].value()
            date = form1['date'].value()
            start_time = form1['start_time'].value()
            end_time = form1['end_time'].value()
            movie_id = form1['movie_id'].value()
            this_show = Show.objects.get(cinema_hall_id=hall_id,date=date,start_time=start_time,
                        end_time=end_time,movie_id=movie_id)

            seats = Cinema_Seat.objects.filter(cinema_hall_id=hall_id)
            for seat in seats:
                s = Show_Seat(is_empty=True,price=70000,cinema_seat_id=seat,show_id=this_show)
                s.save()
            return HttpResponseRedirect('/add_show?submitted=True')
    else:
        form1 = ShowForm
        movies = Movie.objects.all()
        movies_dur = [m.duration for m in movies]
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'ui/add_show.html', {'form1': form1 , 'submitted':submitted, 'movies':movies_dur})

def edit_show(request, show_id):
    show = Show.objects.get(pk =  show_id)
    movies = Movie.objects.all()
    movies_dur = [m.duration for m in movies]
    form = ShowForm(request.POST or None, instance = show)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/show_list')
    return render(request, 'ui/edit_show.html', {'form1': form, 'show':show, 'movies':movies_dur })

def delete_show(request, show_id):
    show = Show.objects.get(pk =  show_id).delete()
    return HttpResponseRedirect('/show_list')
    
def add_cinema(request):
    submitted = False
    if request.method == "POST":
        author = Cinema(total_cinema_halls = 0)
        form = CinemaForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_cinema?submitted=True')
    else:
        form = CinemaForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'ui/add_cinema.html', {'form': form , 'submitted':submitted})

def add_cinema_hall(request):
    submitted = False
    if request.method == "POST":
        author = Cinema_Hall(total_seats = 48)
        form = CinemaHallForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
            for cinema in Cinema.objects.all():
                cinema.total_cinema_halls = len(Cinema_Hall.objects.filter(cinema_id=cinema.id))
                cinema.save()
            
            for cinema_hall in Cinema_Hall.objects.all():
                if len(Cinema_Seat.objects.filter(cinema_hall_id=cinema_hall.id))==0:
                    c = 'ABCDEF'
                    n = {1,2,3,4,5,6,7,8}
                    for cc in c:
                        for nn in n:
                            seat_name = cc + str(nn)
                            seat = Cinema_Seat(seat_name=seat_name, cinema_hall_id=cinema_hall)
                            seat.save()
            return HttpResponseRedirect('/add_cinema_hall?submitted=True')
    else:
        form = CinemaHallForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'ui/add_cinema_hall.html', {'form': form , 'submitted':submitted})

def edit_cinema_hall(request, cinema_hall_id):
    cinema_hall = Cinema_Hall.objects.get(pk = cinema_hall_id)
    form = CinemaHallForm(request.POST or None, instance = cinema_hall)
    if form.is_valid():
        form.save()
        for cinema in Cinema.objects.all():
                cinema.total_cinema_halls = len(Cinema_Hall.objects.filter(cinema_id=cinema.id))
                cinema.save()
        return HttpResponseRedirect('/cinema_list')
    return render(request, 'ui/edit_cinema_hall.html', {'form': form, 'cinema_hall': cinema_hall })

def edit_cinema(request, cinema_id):
    cinema = Cinema.objects.get(pk = cinema_id)
    form = CinemaForm(request.POST or None, instance = cinema)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/cinema_list')
    return render(request, 'ui/edit_cinema.html', {'form': form, 'cinema': cinema })

def delete_cinema(request, cinema_id):
    cinema = Cinema.objects.get(pk =  cinema_id).delete()
    return HttpResponseRedirect('/cinema_list')

def delete_cinema_hall(request, cinema_hall_id):
    cinema_hall = Cinema_Hall.objects.get(pk =  cinema_hall_id).delete()
    for cinema in Cinema.objects.all():
                cinema.total_cinema_halls = len(Cinema_Hall.objects.filter(cinema_id=cinema.id))
                cinema.save()
    return HttpResponseRedirect('/cinema_list')

def add_booking(request):
    submitted = False
    if request.method == "POST":
        form1 = BookingForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/add_booking?submitted=True')
    else:
        form1 = BookingForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'ui/add_booking.html', {'form1': form1 , 'submitted':submitted})

def delete_booking(request, booking_id):
    booking = Booking.objects.get(pk =  booking_id).delete()
    return HttpResponseRedirect('/booking_list')

def add_show_seat(request):
    submitted = False
    if request.method == "POST":
        form1 = Show_SeatForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/add_show_seat?submitted=True')
    else:
        form1 = Show_SeatForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'ui/add_show_seat.html', {'form1': form1 , 'submitted':submitted})

def delete_show_seat(request, show_seat_id):
    show_seat = Show_Seat.objects.get(pk =  show_seat_id).delete()
    return HttpResponseRedirect('/show_seat_list')
#edit

def edit_booking(request, booking_id):
    booking = Booking.objects.get(pk =  booking_id)
    form = BookingForm(request.POST or None, instance = booking)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/booking_list')
    return render(request, 'ui/edit_booking.html', {'form': form, 'show':booking})

def edit_show_seat(request, show_seat_id):
    show_seat = Show_Seat.objects.get(pk =  show_seat_id)
    form = Show_SeatForm(request.POST or None, instance = show_seat)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/show_seat_list')
    return render(request, 'ui/edit_show_seat.html', {'form': form, 'show':show_seat})


def get_movie_info(request, pk):
    # print("?")
    movie = Movie.objects.get(pk=pk)
    cinema_list = Cinema.objects.all()
    show_lists = {}
    for cinema in cinema_list:
        show_lists[cinema.name] = []
        cinema_hall_list = Cinema_Hall.objects.filter(cinema_id=cinema.id)
        for cinema_hall in cinema_hall_list:
            shows = Show.objects.filter(cinema_hall_id=cinema_hall.id,movie_id=movie.id,date__gte=datetime.date.today())
            for s in shows:
                show_lists[cinema.name].append(s)
    print(show_lists)

    return render(request, 'ui/movie_info.html', {'movie':movie, 'shows':show_lists})

def get_show_info(request,pk):
    show = Show.objects.get(pk=pk)
    seat_list = Show_Seat.objects.filter(show_id=pk)
    return render(request, 'ui/show_info.html', {'show':show,'seat_list':seat_list})

def buy_ticket(request):
    seat_ids = request.GET.getlist('id')
    seats = [Show_Seat.objects.get(pk=i) for i in seat_ids]
    total_amount = 0
    for seat in seats:
        total_amount += seat.price
    booking = Booking(number_of_seats=len(seat_ids),timestamp=datetime.date.today(),
                    amount=total_amount, user_id=request.user, show_id=seats[0].show_id)
    booking.save()
    for seat in seats:
        seat.booking_id = booking
        seat.is_empty = False
        seat.save()
    return render(request, 'ui/success_order.html' , {'seats':seats,'booking':booking, 'show':seats[0].show_id})

def search_movie(request):
    if request.method == "POST":
        searched = request.POST['searched']
        movie_list = Movie.objects.filter(title__icontains = searched)
        print(movie_list)
        return render(request, 'ui/movie_list.html', {'movie_list':movie_list})
    else:
        return HttpResponseRedirect('/movie_list')