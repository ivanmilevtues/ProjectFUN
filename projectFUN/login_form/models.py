from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    img = models.CharField(max_length=255, null=True)
    is_king = models.BooleanField(default=False)

