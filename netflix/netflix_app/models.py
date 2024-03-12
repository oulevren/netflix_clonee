from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class NetflixUser(AbstractUser):
    email = models.EmailField(("E-mail Adresi"), max_length=254,unique=True)
    avatar = models.ImageField(("Profil Fotoğrafı"), upload_to="Users/Avatars/")