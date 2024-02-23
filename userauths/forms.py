from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders to form fields
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'