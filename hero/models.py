from django.db import models

# Create your models here.
class SuperHero(models.Model):

    name = models.CharField(max_length=200)

    power = models.CharField(max_length=200)

    universe = models.CharField(max_length=200)

    city = models.CharField(max_length=200)

    team = models.CharField(max_length=200)

    def __str__(self):
        return self.name