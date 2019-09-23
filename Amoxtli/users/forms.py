from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Correo electronico ya esta registrado')
        return email
    
class ProfileCreateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['name']

class UserUpdateForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = ['username']
  
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['name', 'university', 'city']

class AddressUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['city', 'postalCode', 'colonia', 'calle', 'numero']

class CardUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['cardType', 'cardName', 'cardNumber', 'cardBack', 'cardDate']

