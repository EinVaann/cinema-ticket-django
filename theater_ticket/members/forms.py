from email.policy import default
from django import forms
from django.forms import ModelForm,ModelChoiceField
from .models import  Cinema, Cinema_Hall, Movie, Show, Booking, Show_Seat


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        labels = {
            'title' : '',
            'image' : '',
            'description' : '',
            'duration' : '',
            'released_date' : '',
            'genre' : '',
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'description' : forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
            'image' : forms.FileInput(attrs={'class':'form-control'}),
            'duration' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Duration'}),
            'released_date' : forms.DateInput(attrs={'class':'form-control','placeholder':'Realeased date'}),
            'genre' : forms.TextInput(attrs={'class':'form-control','placeholder':'Genre'}),
        }

class CinemaHallField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class MovieField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class ShowField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
    
class ShowForm(ModelForm):
    # cinema_hall_id = CinemaHallField(Cinema_Hall.objects)
    # movie_id = MovieField(Movie.objects)
    class Meta:
        model = Show
        fields = ('date','start_time','end_time','cinema_hall_id','movie_id')

        labels = {
            'date' : '',
            'start_time' : '',
            'end_time' : '',
            'cinema_hall_id':'Cinema Hall',
            'movie_id':'Movie'
        }
        widgets = {
            'date' : forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'start_time' : forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Start Time HH:MM'}),
            'end_time' : forms.TimeInput(attrs={'class':'form-control', 'placeholder':'End Time HH:MM', 'readonly':True }),
        }
        
class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = "__all__"

        labels = {
            'number_of_seats':'',
            'timestamp':'',
            'amount':'',
            'user_id':'User',
            'show_id':'Show'
        }
        widgets = {
            'number_of_seats' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Number of Seats'}),
            'timestamp' : forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Timestamp YYYY-MM-DD'}),
            'amount' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Amount'}),
        }
        
class Show_SeatForm(ModelForm):
    is_empty = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    class Meta:
        model = Show_Seat
        fields = ('is_empty','price','cinema_seat_id','show_id','booking_id')

        labels = {
            'is_empty' : '',
            
        }
        widgets = {
            'price' : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price'}),
        }

class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        fields =  ('name',)
        labels = {
            'name' : ''
        }
        widgets = {
            'name' : forms.TextInput(attrs={ 'placeholder':'Name'}),
        }

class CinemaHallForm(ModelForm):
    class Meta:
        model = Cinema_Hall
        fields = "__all__"
        labels = {
            'name' : '',
            'total_seats':''
        }
        widgets = {
            'name' : forms.TextInput(attrs={ 'placeholder':'Name'}),
            'total_seats':forms.NumberInput(attrs={ 'placeholder':'Number of seats'}),
        }