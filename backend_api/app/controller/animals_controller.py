from app.model.models import Animal

def get_all_animals(request):
    animals=Animal.objects.all().order_by('pk')
    return animals

def get_animal_by_id(request, id_animal):
    animal = Animal.objects.get(ID = id_animal)
    return animal

def get_last_three_animals(request):
    animals=Animal.objects.all().order_by('-entered')[:3]
    return animals