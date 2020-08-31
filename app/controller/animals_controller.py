from app.model.models import Animal

def get_all_animals(request):
    animals=Animal.objects.all().order_by('-entered')
    return animals

def get_animal_by_id(request, id_animal):
    animal = Animal.objects.get(ID = id_animal)
    return animal

def get_last_three_animals(request):
    animals=Animal.objects.filter(visible=True).order_by('-entered')[:3]
    return animals

def change_visibility_of_animal(request, id_animal):
    id_animal = int(id_animal)
    animal=Animal.objects.get(pk=id_animal)
    if animal.visible == True:
        animal.visible = False
    else:
        animal.visible = True
    animal.save()