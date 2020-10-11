from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photos
# Create your views here.
def welcome(request):
    images = Photos.objects.all() 
    return render (request,'index.html',{'images':images})