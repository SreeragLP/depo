from django.db import models

# Create your models here.

class Vihicle(models.Model):
    model_type = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number= models.IntegerField(max_length=50)

def __str__(self):
    return self.model_type

