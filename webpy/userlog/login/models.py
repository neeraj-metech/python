from django.db import models

# Create your models here.


class loginUserDetails(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date = models.DateField()
