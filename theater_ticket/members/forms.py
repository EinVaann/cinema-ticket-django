
from django import forms
from django.forms import ModelForm,ModelChoiceField
from .models import  Movie, Show


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

class ShowForm(ModelChoiceField):
    class Meta:
        model : Show
        field = ('date','start_time','end_time','cinema_hall_id','movie_id')

        labels = {
            'date' : '',
            'start_time' : '',
            'end_time' : '',
            'cinema_hall_id' : '',
            'movie_id' : '',
        }
        widgets = {
            'date' : forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date'}),
            'start_time' : forms.DateTimeInput(attrs={'class':'form-control','placeholder':'Start time'}),
            'end_time' : forms.DateTimeInput(attrs={'class':'form-control','placeholder':'End time'}),
            'cinema_hall_id' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Cinema hall id'}),
            'movie_id' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Movie id'}),
        }