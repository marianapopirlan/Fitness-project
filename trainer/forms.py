from django import forms
from django.forms import TextInput, Textarea, DateTimeInput

from .models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        # fields = '__all__' # preia toate fieldurile din model si in interfata va fi in ordinea declarata in fisierul models.py
        fields = ['cnp', 'name',
                  'email', 'date_of_birth', 'speciality',
                  'description']  # specificam fieldurile pe care le vrem din modelul class in ordinea dorita

        widgets = {
            'cnp': TextInput(attrs={'placeholder': 'Please enter the trainer cnp', 'class': 'form-control'}),
            'name': TextInput(attrs={'placeholder': 'Please enter the trainer name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Please enter the trainer email', 'class': 'form-control'}),
            'date_of_birth': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'speciality': TextInput(attrs={'placeholder': 'Please enter the trainer speciality', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter the trainer description', 'class': 'form-control'}),
        }
