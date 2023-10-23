from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import FarmerUser  

class FarmerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = FarmerUser
        fields = ['username', 'email', 'password1', 'password2'] 

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if FarmerUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already registered.')
        return email

from django import forms

class FarmerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
