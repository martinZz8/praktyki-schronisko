from django.shortcuts import render, redirect
from django.contrib import admin
from app.model.models import Photo, Application
from app.forms import Application_Create
from app.controller.photo_controller import image, images_list, get_thumbnail, get_thumbnails_urls
from app.controller.animals_controller import get_last_three_animals, get_all_animals, get_animal_by_id
from app.controller.news_controller import get_last_five_news, get_all_visible_news, get_news_by_id
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
# Create your views here.


def render_home(request):
    last_animals = get_last_three_animals(request)
    last_animals_thumbnails = get_thumbnails_urls(request, last_animals)
    last_news = get_last_five_news(request)

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(message_email, message + '\n\n Wiadomość od: ' + message_name, settings.EMAIL_HOST_USER, [
            settings.EMAIL_HOST_USER], fail_silently=False)
        # if message_name is not None:
        #     messages.info(request,"")
        return render(request, 'app/home.html', {'last_animals': last_animals, 'last_animals_thumbnails': last_animals_thumbnails, 'last_news': last_news, 'message_name': message_name})
    else:
        return render(request, 'app/home.html', {'last_animals': last_animals, 'last_animals_thumbnails': last_animals_thumbnails, 'last_news': last_news})

    # return render(request, 'app/home.html', {'last_animals': last_animals, 'last_animals_thumbnails': last_animals_thumbnails, 'last_news': last_news})


def render_news(request):
    news = get_all_visible_news(request)
    return render(request, 'app/news.html', {'news': news})


def render_post(request, id_post):
    id_post = int(id_post)
    post = get_news_by_id(request, id_post)
    return render(request, 'app/post.html', {'post': post})


def render_animals(request):
    animals = get_all_animals(request)

    type_query = request.GET.get('type')
    race_query = request.GET.get('race')
    sex_query = request.GET.get('sex')
    
    if type_query != '' and type_query is not None:
        animals = animals.filter(type__exact=type_query.strip())
    if race_query != '' and race_query is not None:
        animals = animals.filter(race__icontains=race_query.strip())
    if sex_query != '' and sex_query is not None:
        animals = animals.filter(sex__exact=sex_query.strip())

    animals_thumbnails = get_thumbnails_urls(request, animals)
    return render(request, 'app/animals.html', {'animals':animals, 'animals_thumbnails':animals_thumbnails})


def render_animal(request, id_animal):
    id_animal = int(id_animal)
    animal = get_animal_by_id(request, id_animal)
    thumbnail = get_thumbnail(request, id_animal)
    photos = images_list(request, id_animal)
    return render(request, 'app/animal.html', {'animal': animal, 'thumbnail': thumbnail, 'photos': photos})


def render_application(request, id_animal):
    id_animal = int(id_animal)
    if request.method == "POST":
        form = Application_Create(request.POST or None)
        if form.is_valid():
            animal = get_animal_by_id(request, id_animal)
            name = form.cleaned_data.get("name")
            surname = form.cleaned_data.get("surname")
            email = form.cleaned_data.get("email")
            info = form.cleaned_data.get("info")
            obj = Application.objects.create(
                name=name,
                surname=surname,
                email=email,
                info=info,
                animal=animal
            )
            obj.save()
            return redirect('animal', id_animal=id_animal)
    else:
        form = Application_Create()
    return render(request, 'app/app.html', {'addapp': form, 'animal': id_animal})


# def contact(request):
#     if request.method == "POST":
#         message_name = request.POST['message-name']
#         message_email = request.POST['message-email']
#         message = request.POST['message']

#         send_mail(message_email, message + '\n\n Wiadomość od: ' + message_name, settings.EMAIL_HOST_USER, [
#             settings.EMAIL_HOST_USER], fail_silently=False)
#         return render(request, 'app/home.html', {'message_name': message_name})
#     else:
#         return render(request, 'app/home.html')
