from django.shortcuts import render
from app.model.models import Photo
from app.controller.photo_controller import image, images_list, get_thumbnail, get_thumbnails_urls
from app.controller.animals_controller import get_last_three_animals, get_all_animals, get_animal_by_id
from app.controller.news_controller import get_last_five_news, get_all_visible_news, get_news_by_id

# Create your views here.

def render_home(request):
    last_animals = get_last_three_animals(request)
    last_animals_thumbnails = get_thumbnails_urls(request, last_animals)
    last_news = get_last_five_news(request)
    return render(request, 'app/home.html', {'last_animals':last_animals, 'last_animals_thumbnails':last_animals_thumbnails, 'last_news':last_news})

def render_news(request):
    news = get_all_visible_news(request)
    return render(request, 'app/news.html', {'news':news})

def render_post(request, id_post):
    id_post = int(id_post)
    post = get_news_by_id(request, id_post)
    return render(request, 'app/post.html', {'post':post})

def render_animals(request):
    animals = get_all_animals(request)
    animals_thumbnails = get_thumbnails_urls(request, animals)
    return render(request, 'app/animals.html', {'animals':animals, 'animals_thumbnails':animals_thumbnails})

def render_animal(request, id_animal):
    id_animal = int(id_animal)
    animal = get_animal_by_id(request, id_animal)
    thumbnail = get_thumbnail(request, id_animal)
    photos = images_list(request, id_animal)
    return render(request, 'app/animal.html', {'animal':animal, 'thumbnail':thumbnail, 'photos':photos})