from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name','address','city','phone','image')
        labels = {
            'name': 'F.I.O',
            'address': 'Manzil',
            'city': 'Shahar/tuman',
            'phone': 'Telefon raqam',
            'image': "Tug'ilganlik haqida guvohnoma yoki passport",
        }
        widgets = {
            'name': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'name', 'name':'name'}),
            'address': forms.Select(attrs={'class':'form-control', 'name':'location', 'id':'filial'}),
            'city': forms.Select(attrs={'class':'form-control', 'name':'location2', 'id':'shahar'}),
            'phone': forms.TextInput(attrs={'type':'phone', 'class':'form-control', 'id':'phone', 'name':'phone'}),
            'image': forms.FileInput(attrs={'type':'file', 'name':'image', 'id':'image'})
        }