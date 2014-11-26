from django import forms
from models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'start_day', 'start_time', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'start_day': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Day'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Time'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }