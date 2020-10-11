from django.contrib import admin
from .models import Photos,Location,Category
# Register your models here.

admin.site.register(Photos)
admin.site.register(Category)
admin.site.register(Location)