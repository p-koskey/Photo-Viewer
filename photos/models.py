from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name=value)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    cityname = models.CharField(max_length =30)

    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(cityname=value)

    def __str__(self):
        return self.cityname

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Photos(models.Model):
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =60)
    categorytags = models.ManyToManyField(Category)
    locationtags = models.ManyToManyField(Location)
    image = CloudinaryField('image')
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_by_category(cls, category):
        photos = cls.objects.filter(categorytags__name__icontains=category)
        return photos
        
    @classmethod
    def update_photo(cls, id, value):
        cls.objects.filter(id=id).update(photo=value)

    @classmethod
    def get_photo_by_id(cls, id):
        photo = cls.objects.filter(id=id).all()
        return photo

    @classmethod
    def filter_by_location(cls, location):
        photo_location = Photos.objects.filter(locationtags__name=location).all()
        return photo_location

    def __str__(self):
        return self.name
    class meta:
        ordering =['date']

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()