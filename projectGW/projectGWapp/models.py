from django.db import models

# Create your models here.
from django.db import models


class Dogs(models.Model):
    name = models.CharField(max_length=100)
    Breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
