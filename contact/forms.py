from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': "input form-control", 'placeholder': ' نام خود را وارد کنید'}),
            'email': forms.EmailInput(attrs={'class': "input form-control", 'placeholder': ' ایمیل خود را وادر کنید'}),
            'message': forms.Textarea(attrs={'class': "input form-control", 'rows': '4', 'placeholder': 'پیغام خود را بگذارید'}),
        }