from .models import Photo

def image(request, p_key):
    image_file = Photo.objects.get(pk=p_key)
    return image_file

def images_list(request, f_key):
    image_file = []
    image_file = Photo.objects.filter(animal=f_key)
    return image_file

def get_thumbnail(request, f_key):
    image_file = []
    image_file = Photo.objects.filter(animal=f_key, thumbnail = True)
    if len(image_file) == 0:
        tab = Photo.objects.get(image = "image/brak_zdjecia.png")
        return tab
    return image_file[0]