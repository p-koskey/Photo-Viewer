from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photos
# Create your views here.

def welcome(request):
    images = Photos.objects.all()
    return render (request,'index.html',{'images':images})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos =Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

