from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=264, unique=True)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)

    def __str__(self):
        return self.name
