from django.shortcuts import render
from django.db.models import Q
from app.model.models import Photo, Animal, News, Application
from app.controller.photo_controller import image, images_list, get_thumbnail, get_thumbnails_urls, change_thumbnail
from app.controller.news_controller import get_all_news, get_news_by_id
from app.controller.animals_controller import get_all_animals, get_animal_by_id, change_visibility_of_animal
from app.controller.applications_controller import get_all_app, get_app_by_id
from app.forms import New_Create, Animal_Create, Photo_create
import requests
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.info(
                request, 'Nieprawidłowa nazwa użytkownika lub hasło!')
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('home')


def render_thumbnail(request):
    if request.user.is_authenticated:
        image_file = get_thumbnail(request, 1)
        return render(request, 'adminpages/adminpage.html', {'images': image_file})
    else:
        return redirect('login')


def render_adminanimals(request):
    animals = get_all_animals(request)

    name_query = request.GET.get('name')
    race_query = request.GET.get('race')
    sex_query = request.GET.get('sex')
    type_query = request.GET.get('type')
    date1_query = request.GET.get('date1')
    date2_query = request.GET.get('date2')

    if name_query != '' and name_query is not None:
        animals = animals.filter(name__icontains=name_query.strip())
    if race_query != '' and race_query is not None:
        animals = animals.filter(race__icontains=race_query.strip())
    if sex_query != '' and sex_query is not None:
        animals = animals.filter(sex__exact=sex_query.strip())
    if type_query != '' and type_query is not None:
        animals = animals.filter(type__exact=type_query.strip())
    if date1_query != '' and date1_query is not None:
        animals = animals.filter(entered__gte=datetime.strptime(
            date1_query.strip(), '%d-%m-%Y').strftime('%Y-%m-%d %H:%M'))
    if date2_query != '' and date2_query is not None:
        animals = animals.filter(entered__lte=datetime.strptime(
            date2_query.strip(), '%d-%m-%Y').strftime('%Y-%m-%d %H:%M'))

    thumbnails_urls = get_thumbnails_urls(request, animals)
    page = request.GET.get('page', 1)
    paginator = Paginator(animals, 6)
    try:
        animal = paginator.page(page)
    except PageNotAnInteger:
        animal = paginator.page(1)
    except EmptyPage:
        animal = paginator.page(paginator.num_pages)
    return render(request, 'adminpages/adminanimals.html', {'animals': animal, 'thumbnails': thumbnails_urls})


def render_adminnews(request):
    news = get_all_news(request)
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 3)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'adminpages/adminnews.html', {'news': news})


def render_addnews(request):
    form = New_Create(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('adminnews')
    return render(request, 'adminpages/addnews.html', {'addnews': form})


def render_news_delete(request, id_news):
    id_news = int(id_news)
    try:
        news = News.objects.get(ID=id_news)
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
    news_form = New_Create(request.POST or None,
                           request.FILES or None, instance=news)
    if news_form.is_valid():
        news_form.save()
        return redirect('adminnews')
    return render(request, 'adminpages/addnews.html', {'addnews': news_form})


def render_adminapplications(request):
    app = get_all_app(request)
    page = request.GET.get('page', 1)
    paginator = Paginator(app, 7)
    try:
        app = paginator.page(page)
    except PageNotAnInteger:
        app = paginator.page(1)
    except EmptyPage:
        app = paginator.page(paginator.num_pages)
    return render(request, 'adminpages/adminapplications.html', {'applications': app})


def render_app_delete(request, id_app):
    id_app = int(id_app)
    try:
        app = get_app_by_id(request, id_app)
    except Application.DoesNotExist:
        return redirect('applications')
    app.delete()
    return redirect('applications')


def render_addanimal(request):
    form = Animal_Create(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('adminanimals')
    return render(request, 'adminpages/addanimal.html', {'addanimal': form})


def render_animal_delete(request, id_animal):
    id_animal = int(id_animal)
    try:
        animal = Animal.objects.get(ID=id_animal)
    except Animal.DoesNotExist:
        return redirect('adminanimals')
    animal.delete()
    return redirect('adminanimals')


def render_animal_update(request, id_animal):
    id_animal = int(id_animal)
    try:
        animal = get_animal_by_id(request, id_animal)
    except Animal.DoesNotExist:
        return redirect('adminanimals')
    animal_form = Animal_Create(request.POST or None, instance=animal)
    if animal_form.is_valid():
        animal_form.save()
        return redirect('adminanimals')
    return render(request, 'adminpages/addanimal.html', {'addanimal': animal_form})


def render_admin_photos(request, id_animal):
    id_animal = int(id_animal)
    photos = images_list(request, id_animal)
    if request.method == "POST":
        form = Photo_create(request.POST, request.FILES)
        if form.is_valid():
            animal = get_animal_by_id(request, id_animal)
            image = form.cleaned_data.get("img")
            obj = Photo.objects.create(
                animal=animal,
                image=image
            )
            obj.save()
    else:
        form = Photo_create()
    return render(request, 'adminpages/adminphotos.html', {'photos': photos, 'form_photo': form})


def render_photo_delete(request, id_photo):
    id_photo = int(id_photo)
    try:
        photo = image(request, id_photo)
    except Photo.DoesNotExist:
        return redirect('adminphotos', id_animal=photo.animal.ID)
    photo.delete()
    return redirect('adminphotos', id_animal=photo.animal.ID)


def render_select_thumbnail(request, id_animal):
    photos = images_list(request, id_animal)
    return render(request, 'adminpages/selectthumbnail.html', {'photos': photos})


def render_change_thumbnail(request, id_photo):
    change_thumbnail(request, id_photo)
    return redirect('adminanimals')


def change_animal_visibility(request, id_animal):
    change_visibility_of_animal(request, id_animal)
    return redirect('adminanimals')
