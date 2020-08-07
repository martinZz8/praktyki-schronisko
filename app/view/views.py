from django.shortcuts import render
from app.model.models import Photo
from app.controller.photo_controller import image, images_list, get_thumbnail, get_thumbnails_urls
from app.controller.animals_controller import get_last_three_animals
from app.controller.news_controller import get_last_five_news

# Create your views here.

def render_home(request):
    last_animals = get_last_three_animals(request)
    last_animals_thumbnails = get_thumbnails_urls(request, last_animals)
    last_news = get_last_five_news(request)
    return render(request, 'app/home.html', {'last_animals':last_animals, 'last_animals_thumbnails':last_animals_thumbnails, 'last_news':last_news})