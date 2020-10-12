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
        
        self.newImage = Photos(name = 'Canoeing',description = 'Love trees',image='gzxzdfhashdfhas')

        self.newImage.save_photo()
        self.newImage.categorytags.add(self.newCategory)
        self.newImage.locationtags.add(self.newLocation)

       

    def test_instance(self):
        self.assertTrue(isinstance(self.newImage, Photos))

    def test_delete_photo(self):
        self.newImage.delete_photo()
        photos = Photos.objects.all()
        self.assertTrue(len(photos) == 0)

    def test_update_photo(self):
        self.newImage.save_photo()
        self.newImage.update_photo(self.newImage.id, 'photos/img.jpg')
        new_img = Photos.objects.filter(image='photos/img.jpg')
        self.assertTrue(len(new_img) > 0)

    def test_get_photo_by_id(self):
        res = self.newImage.get_photo_by_id(self.newImage.id)
        photo = Photos.objects.filter(id=self.newImage.id)
        self.assertTrue(res, photo)

    def test_search_photo_by_location(self):
        self.newImage.save_photo()
        res = self.newImage.filter_by_location(location='Nairobi')
        self.assertTrue(len(res) == 1)

    def test_search_photo_by_category(self):
        self.newImage.save_photo()
        res = self.newImage.search_by_category(category='Nature')
        self.assertTrue(len(res) > 0)

    def tearDown(self):
        Photos.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

class CategoryTestClass(TestCase):

    def setUp(self):
        self.category = Category(name='Nature')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

