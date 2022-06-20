
from django import forms
from django.forms import ModelForm,ModelChoiceField
from .models import  Cinema_Hall, Movie, Show


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title','description','duration','released_date','genre')
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

class ShowForm(ModelForm):
    cinema_hall_id = CinemaHallField(Cinema_Hall.objects)
    movie_id = MovieField(Movie.objects)
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