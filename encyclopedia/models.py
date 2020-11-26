from django.contrib.auth.models import AbstractUser
from django.db import models

class Wiki(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()

class edit_page(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()