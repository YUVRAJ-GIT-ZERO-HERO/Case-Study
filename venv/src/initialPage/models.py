from django.db import models

# Create your models here.
class GeometryModel(models.Model):
    location = models.CharField(max_length=200)
