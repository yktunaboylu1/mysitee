from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.TextField(max_length=500, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True, default='')
    image = models.ImageField(max_length=100, upload_to='user', default='noimage.jpg')
    phone = models.CharField(max_length=15, blank=True, default='')

    def __str__(self):
        return str(self.user)
