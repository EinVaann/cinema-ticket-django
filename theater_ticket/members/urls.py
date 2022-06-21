from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home_page_view, name= 'home'),
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
    path('add_movie',views.add_movie, name='add_movie'),
    path('edit_movie/<movie_id>',views.edit_movie, name='edit_movie'),
    path('admin_page',views.admin_page, name='admin_page'),
    path('add_show',views.add_show, name='add_show'),
    path('edit_show/<show_id>',views.edit_show, name='edit_show'),
    path('add_cinema',views.add_cinema, name='add_cinema'),
    path('edit_cinema/<cinema_id>',views.edit_cinema, name='edit_cinema'),
    path('add_booking',views.add_booking, name='add_booking'),
    path('add_show_seat',views.add_show_seat, name='add_show_seat'),
    path('add_payment',views.add_payment, name='add_payment'),
    path('edit_booking/<booking_id>',views.edit_booking, name='edit_booking'),
    path('edit_show_seat/<show_seat_id>',views.edit_show_seat, name='edit_show_seat'),
    path('edit_payment/<payment_id>',views.edit_payment, name='edit_payment'),
    path('movie_info/<str:pk>/', views.get_movie_info, name='movie_info'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)