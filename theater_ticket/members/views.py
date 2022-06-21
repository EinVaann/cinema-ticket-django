from os import device_encoding
from tkinter import N 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import MovieForm, ShowForm , BookingForm ,Show_SeatForm, PaymentForm
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

def get_all_payment(request):
    payment_list = Payment.objects.all()
    return render(request, 'ui/payment_list.html', {'payment_list':payment_list}) 
    
def get_all_movies(request):
    movie_list = Movie.objects.all()
    return render(request, 'ui/movie_list.html', {'movie_list':movie_list})

def home_page_view(request):
    movies = Movie.objects.all()
    if len(movies) > 10:
        movies = movies[:10]
    return render(request, 'ui/home.html', {'movies':movies})

def create_seats(request):
    cinema_halls = Cinema_Hall.objects.all()
    
    c = 'ABCDEFGHJK'
    n = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
    for cinema_hall in cinema_halls:
        d = 0
        for cc in c:
            for nn in n:
                if cc!='K' and nn>11:
                    continue
                seat_name = cc + str(nn)
                # print(seat_name)
                # d+=1
                seat = Cinema_Seat(seat_name=seat_name, cinema_hall_id=cinema_hall)
                seat.save()
        # print(d)
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


def add_show(request):
    submitted = False
    if request.method == "POST":
        form1 = ShowForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/add_show?submitted=True')
    else:
        form1 = ShowForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'ui/add_show.html', {'form1': form1 , 'submitted':submitted})

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


def add_payment(request):
    submitted = False
    if request.method == "POST":
        form1 = PaymentForm(request.POST)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect('/add_payment?submitted=True')
    else:
        form1 = PaymentForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'ui/add_payment.html', {'form1': form1 , 'submitted':submitted})


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

def edit_payment(request, payment_id):
    payment = Payment.objects.get(pk =  payment_id)
    form = PaymentForm(request.POST or None, instance = payment)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/payment_list')
    return render(request, 'ui/edit_payment.html', {'form': form, 'show':payment})