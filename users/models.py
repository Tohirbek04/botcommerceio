from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=13, null=True)
    image = models.ImageField(upload_to='users', null=True)

