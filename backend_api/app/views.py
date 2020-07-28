from django.shortcuts import render
from .models import Photo

# Create your views here.

def image(request):
    image_file = Photo.objects.get(pk=4)
    return render(request, 'app/test.html', {'zdjecie':image_file})