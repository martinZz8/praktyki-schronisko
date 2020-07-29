from django.shortcuts import render
from .models import Photo, Animal
from .photo_views import image, images_list, get_thumbnail

def render_thumbnail(request):
    image_file = get_thumbnail(request, 1)
    return render(request, 'adminpages/adminpage.html', {'images':image_file})

def admin_animal_retrieve(request):
    animals=Animal.objects.all()
    thumbnails = []
    for animal in animals:
        thumbnails.append(get_thumbnail(request, animal.ID))
    return render(request, 'adminpages/adminanimals.html', {'animals':animals, 'thumbnails':thumbnails})