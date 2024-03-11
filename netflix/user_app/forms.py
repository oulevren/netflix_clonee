from django import forms
from netflix_app.models import *

class UserForm(forms.ModelForm):

    email = forms.CharField(label="",widget=forms.EmailInput(attrs={'placeholder':"E-mail ADRESİ"}))
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder': 'sifre'}))


    class Meta:
        model = NetflixUser
        fields = ["email","username","password"]

        # help_texts = {
        #     'username': None,
        #     'password': None
        # }

        # labels = {
        #     'password' : "",
        #     'username': "",
        # }

    