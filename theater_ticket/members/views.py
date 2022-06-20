from os import device_encoding
from tkinter import N
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import MovieForm, ShowForm
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

    
def get_all_movies(request):
    movie_list = Movie.objects.all()
    return render(request, 'ui/movie_list.html', {'movie_list':movie_list})

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
