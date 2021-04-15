from django import forms
from django.contrib.auth.models import User

from spencersapp.models import BaseClass


class myform(forms.ModelForm):
    class Meta:
        model = BaseClass

        fields = '__all__'



class singnupform(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)
     email = forms.EmailField(max_length=200)
     first_name=forms.CharField(max_length=10)
     last_name=forms.CharField(max_length=10)

     class Meta:
         model = User
         fields = ['username', 'password', 'email', 'first_name', 'last_name']


'''password validation'''
def clean_password(self):
  password = self.cleaned_data['password']
  if len(password) < 4:
      raise forms.ValidationError("password is too short")
  return password


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'email', 'first_name', 'last_name']

class passwordchangeform(forms.ModelForm):
    class Meta:
        model=User
        fields=['password']