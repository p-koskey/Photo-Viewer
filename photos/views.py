from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photos,Location
# Create your views here.

def welcome(request):
    images = Photos.objects.all()
    locations = Location.get_locations()
    return render (request,'index.html',{'images':images, 'locations':locations})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos =Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def locationimages(request,location):

    locationimages = Photos.filter_by_location(location)
    return render(request, 'location.html', {'images': locationimages})