from django.db import models

# Create your models here.
class Programers(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=254)
    position = models.CharField(max_length=254)
