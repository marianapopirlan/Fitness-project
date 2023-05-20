from django import forms
from django.forms import TextInput, Textarea, DateTimeInput

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        # fields = '__all__' # preia toate fieldurile din model si in interfata va fi in ordinea declarata in fisierul models.py
        fields = ['cnp', 'name',
                  'email', 'date_of_birth',
                  'join_date', 'expiry_date']  # specificam fieldurile pe care le vrem din modelul class in ordinea dorita

        widgets = {
            'cnp': TextInput(attrs={'placeholder': 'Please enter the member CNP', 'class': 'form-control'}),
            'name': TextInput(attrs={'placeholder': 'Please enter the member name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Please enter the member email', 'class': 'form-control'}),
            'date_of_birth': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'join_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiry_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
