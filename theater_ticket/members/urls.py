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
    # path('create_seats', views.create_seats),
    # path('delete_seats', views.delete_seats),
    path('add_movie',views.add_movie, name='add_movie'),
    path('edit_movie/<movie_id>',views.edit_movie, name='edit_movie'),

    path('add_cinema',views.add_cinema, name='add_cinema'),
    
    path('admin_page',views.admin_page, name='admin_page'),
    path('add_show',views.add_show, name='add_show'),
    path('edit_show/<show_id>',views.edit_show, name='edit_show')
]