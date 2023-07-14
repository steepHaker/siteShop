from django import forms
from .models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeatpassword']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'repeatpassword': forms.PasswordInput(attrs={'placeholder': 'Repeat Password'})
        }
     