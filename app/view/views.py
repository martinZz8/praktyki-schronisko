from django.shortcuts import render
from app.model.models import Photo
from app.controller.photo_controller import image, images_list, get_thumbnail

# Create your views here.

def rendertest(request):
    image_file = images_list(request, 2)
    return render(request, 'app/test.html', {'zdjecie':image_file})
    
def rendertest2(request):
    image_file = get_thumbnail(request, 1)
    return render(request, 'app/test2.html', {'images':image_file})

def render_base(request):
    image_file = get_thumbnail(request, 1)
    return render(request, 'app/base.html', {'images':image_file})