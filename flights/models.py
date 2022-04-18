from django.db import models
from django.template import Origin

class Flight(models.Model):
    title = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration= models.IntegerField()



def __str__(self):
    return self.title