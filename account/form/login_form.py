from django import forms
from django.contrib.auth.models import User as userModel


class LoginForm(forms.ModelForm):

    class Meta:
        model = userModel
        fields = ('username', 'password',)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}))
