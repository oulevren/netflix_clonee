from django.db import models
from django.contrib.auth.models import User,AbstractUser,AbstractBaseUser,Group,Permission

# Create your models here.


class NetflixUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='netflix_users')
    user_permissions = models.ManyToManyField(Permission, related_name='netflix_users_permissions')
    email = models.EmailField(("E-mail adresi"), max_length=254,unique=True)
    avatar = models.ImageField(("Profil Fotoğrafı"), upload_to="User/Avatars/")