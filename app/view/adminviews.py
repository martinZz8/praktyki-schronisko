from django.shortcuts import render
from app.model.models import Photo, Animal, News, Application
from app.controller.photo_controller import image, images_list, get_thumbnail, get_thumbnails_urls
from app.controller.news_controller import get_all_news, get_news_by_id
from app.controller.animals_controller import get_all_animals
from app.controller.applications_controller import get_all_app, get_app_by_id
from app.forms import New_Create
import requests
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

def render_thumbnail(request):
    image_file = get_thumbnail(request, 1)
    return render(request, 'adminpages/adminpage.html', {'images':image_file})

def render_adminanimals(request):
    animals=get_all_animals(request)
    thumbnails_urls = get_thumbnails_urls(request, animals)
    return render(request, 'adminpages/adminanimals.html', {'animals':animals, 'thumbnails':thumbnails_urls})

def render_adminnews(request):
    news=get_all_news(request)
    return render(request, 'adminpages/adminnews.html', {'news':news})

def render_addnews(request):
    form = New_Create(request.POST or None)
    if form.is_valid():
       form.save()
       return redirect('adminnews')
    return render(request, 'adminpages/addnews.html', {'addnews':form})

def render_news_delete(request, id_news):
    id_news = int(id_news)
    try:
        news = News.objects.get(ID = id_news)
    except News.DoesNotExist:
        return redirect('adminnews')
    news.delete()
    return redirect('adminnews')

def render_news_update(request, id_news):
    id_news = int(id_news)
    try:
        news = get_news_by_id(request, id_news)
    except News.DoesNotExist:
        return redirect('adminnews')
    news_form = New_Create(request.POST or None, instance = news)
    if news_form.is_valid():
       news_form.save()
       return redirect('adminnews')
    return render(request, 'adminpages/addnews.html', {'addnews':news_form})

def render_adminapplications(request):
    app=get_all_app(request)
    return render(request, 'adminpages/adminapplications.html', {'applications':app})

def render_app_delete(request, id_app):
    id_app = int(id_app)
    try:
        app = get_app_by_id(request, id_app)
    except Application.DoesNotExist:
        return redirect('applications')
    app.delete()
    return redirect('applications')