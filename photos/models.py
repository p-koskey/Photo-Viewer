from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =60)

    def __str__(self):
        return self.name

class Location(models.Model):
    cityname = models.CharField(max_length =60)

    def __str__(self):
        return self.cityname

class Photos(models.Model):
    name = models.CharField(max_length =60)
    caption = models.CharField(max_length =60)
    categorytags = models.ManyToManyField(Category)
    locationtags = models.ManyToManyField(Location)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name