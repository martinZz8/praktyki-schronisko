from app.model.models import Animal

def get_all_animals(request):
    animals=Animal.objects.all()
    return animals