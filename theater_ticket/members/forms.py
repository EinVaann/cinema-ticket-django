from email.policy import default
from django import forms
from django.forms import ModelForm,ModelChoiceField
from .models import  Cinema_Hall, Movie, Show, Booking, Show_Seat, Payment


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        labels = {
            'title' : '',
            'description' : '',
            'duration' : '',
            'released_date' : '',
            'genre' : '',
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'description' : forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}),
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
        }
        widgets = {
            'date' : forms.DateInput(),
            'start_time' : forms.DateTimeInput(),
            'end_time' : forms.DateTimeInput(),
        }
        
class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ('number_of_seats','timestamp','status','user_id','show_id')

        labels = {
            
        }
        widgets = {
            'number_of_seats' : forms.NumberInput(),
            'timestamp' : forms.DateTimeInput(),
            'status' : forms.NumberInput(),
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
            'price' : forms.NumberInput(),
        }
        
class PaymentForm(ModelForm):

    class Meta:
        model = Payment
        fields = ('amount','timestamp','payment_method','booking_id')

        labels = {
            
        }
        widgets = {
            'amount' : forms.NumberInput(),
            'timestamp' : forms.DateTimeInput(),
            'payment_method' : forms.TextInput(),
        }