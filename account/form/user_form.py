from django import forms
from django.contrib.auth.models import User as userModel


class UserForm(forms.ModelForm):

    class Meta:
        model = userModel
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'is_active',)

        widgets = {
            'username': forms.TextInput(attrs= {'class': 'form-control', 'color': 'red !important'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': ''}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
