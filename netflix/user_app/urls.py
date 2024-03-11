from django.contrib import admin
from django.urls import path
from netflix.urls import *
from .views import *

urlpatterns = [
    path('register',register_page,name="register-page"),
    path('login',login_page,name="login-page")
]
