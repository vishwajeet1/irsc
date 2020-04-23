from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=11)
    password = models.CharField(max_length=65)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
