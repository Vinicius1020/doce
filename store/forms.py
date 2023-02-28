from django import forms
from . models import Bolo_search

class Bolo_search_form(forms.ModelForm):
    name_of_perfume = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Ex: bolo', 'style': 'border-radius: 30px'
    }))
    class Meta:
        model = Bolo_search
        fields = ['name_of_perfume',]