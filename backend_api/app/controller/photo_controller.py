from app.model.models import Photo, Animal

def image(request, p_key):
    image_file = Photo.objects.get(pk=p_key)
    return image_file

def images_list(request, f_key):
    image_file = []
    image_file = Photo.objects.filter(animal=f_key).order_by('pk')
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

def change_thumbnail(request, id_photo):
    id_photo = int(id_photo)
    thumbnail_photo=Photo.objects.get(pk=id_photo)
    Photo.objects.filter(animal=thumbnail_photo.animal.ID).exclude(pk = id_photo).update(thumbnail=False)
    thumbnail_photo.thumbnail=True
    thumbnail_photo.save()
