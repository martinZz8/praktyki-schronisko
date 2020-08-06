from django.shortcuts import render
from app.model.models import Photo
from app.controller.photo_controller import image, images_list, get_thumbnail, get_thumbnails_urls
from app.controller.animals_controller import get_last_three_animals

# Create your views here.

def rendertest(request):
    image_file = images_list(request, 2)
    return render(request, 'app/test.html', {'zdjecie':image_file})
    
def rendertest2(request):
    image_file = get_thumbnail(request, 1)
    return render(request, 'app/test2.html', {'images':image_file})

def render_home(request):
    last_animals = get_last_three_animals(request)
    last_animals_thumbnails = get_thumbnails_urls(request, last_animals)
    return render(request, 'app/home.html', {'last_animals':last_animals, 'last_animals_thumbnails':last_animals_thumbnails})