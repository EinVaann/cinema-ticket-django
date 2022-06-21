from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name= 'home'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('cinema_list', views.get_all_cinemas, name='cinema_list'),
    path('cinema_info/<str:pk>/', views.get_cinema, name='cinema_info'),
    path('movie_list', views.get_all_movies, name='movie_list'),
    path('show_list', views.get_all_show, name='show_list'),
    path('booking_list', views.get_all_booking, name='booking_list'),
    path('show_seat_list', views.get_all_show_seat, name='show_seat_list'),
    path('payment_list', views.get_all_payment, name='payment_list'),
    # path('create_seats', views.create_seats),
    # path('delete_seats', views.delete_seats),
    path('add_movie',views.add_movie, name='add_movie'),
    path('admin_page',views.admin_page, name='admin_page'),
    path('add_show',views.add_show, name='add_show'),
    path('add_booking',views.add_booking, name='add_booking'),
    path('add_show_seat',views.add_show_seat, name='add_show_seat'),
    path('add_payment',views.add_payment, name='add_payment'),
    #edit
    path('edit_booking/<booking_id>',views.edit_booking, name='edit_booking'),
    path('edit_show_seat/<show_seat_id>',views.edit_show_seat, name='edit_show_seat'),
    path('edit_payment/<payment_id>',views.edit_payment, name='edit_payment'),
]