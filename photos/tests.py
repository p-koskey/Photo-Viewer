from django.test import TestCase
from .models import Photos,Location,Category

# Create your tests here.
class PhotoTestClass(TestCase):

     #set up
    def setUp(self):
        #create Category Tag
        self.newCategory = Category(name='Nature')
        self.newCategory.save_category()

        #Create Location Tag
        self.newLocation = Location(cityname='Nairobi')
        self.newLocation.save_location()
        
        self.newImage = Photos(name = 'Canoeing',caption = 'Love trees',categorytags=self.newCategory,locationtags=self.newLocation,image='gzxzdfhashdfhas')
        
        self.newImage.save_photo()

       

    def test_instance(self):
        self.assertTrue(isinstance(self.newImage, Image))

    def tearDown(self):
        Photos.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
