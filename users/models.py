from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=300)
