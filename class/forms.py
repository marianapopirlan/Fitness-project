from django import forms
from django.forms import TextInput, Textarea, DateTimeInput

from .models import Class
from trainer.models import Trainer


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        # fields = '__all__' # preia toate fieldurile din model si in interfata va fi in ordinea declarata in fisierul models.py
        fields = ['id', 'name',
                  'trainer', 'date',
                  'description']  # specificam fieldurile pe care le vrem din modelul class in ordinea dorita

        widgets = {
            'id': TextInput(attrs={'placeholder': 'Please enter the class id', 'class': 'form-control'}),
            'name': TextInput(attrs={'placeholder': 'Please enter the class name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter the class description', 'class': 'form-control',
                                           'rows': 3, 'type': 'textarea'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),

        }

    trainer = forms.ModelChoiceField(
        label="Trainer",
        widget=forms.Select(
            attrs={'class': 'form-select', 'id': 'trainer'},
        ),
        queryset=Trainer.objects.all()
    )
