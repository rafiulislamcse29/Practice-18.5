from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class RegisterForm(UserCreationForm):
  # def __init__(self, *args, **kwargs):
  #       super(UserCreationForm, self).__init__(*args, **kwargs)
  #       for fieldname in ['username','first_name','email','password1','password2']:
  #         self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
  
  first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'requred','class': 'form-control'}))
  last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'requred','class': 'form-control'}))
  email=forms.CharField(widget=forms.EmailInput(attrs={'id':'requred','class': 'form-control'}))
  # password1=forms.CharField(widget=forms.PasswordInput(attrs={'id':'requred','class': 'form-control'}))
  # password2=forms.CharField(widget=forms.PasswordInput(attrs={'id':'requred','class': 'form-control'}))
  username=forms.CharField(widget=forms.TextInput(attrs={'id':'requred','class': 'form-control'}))
  class Meta:
     model=User
     fields=['username','first_name','last_name','email']
    

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']