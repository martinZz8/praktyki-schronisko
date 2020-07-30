from app.model.models import Photo, Animal

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
        return "/static/images/brak_zdjecia.png" 
    return image_file[0].image.url

def get_thumbnails_urls(request, animals):
    thumbnails_urls = []
    for animal in animals:
        thumbnails_urls.append(get_thumbnail(request, animal.ID))
    return thumbnails_urls