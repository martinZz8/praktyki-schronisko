from django.shortcuts import render
from .models import Photo, Animal, News
from .photo_views import image, images_list, get_thumbnail
from .forms import New_Create
import requests
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def render_thumbnail(request):
    image_file = get_thumbnail(request, 1)
    return render(request, 'adminpages/adminpage.html', {'images':image_file})

def admin_animal_retrieve(request):
    animals=Animal.objects.all()
    thumbnails = []
    for animal in animals:
        thumbnails.append(get_thumbnail(request, animal.ID))
    return render(request, 'adminpages/adminanimals.html', {'animals':animals, 'thumbnails':thumbnails})

def admin_news_retrieve(request):
    news=News.objects.all()
    return render(request, 'adminpages/adminnews.html', {'news':news})

def new_news(request):
    form = New_Create(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('adminnews')
    return render(request, 'adminpages/addnews.html', {'addnews':form})