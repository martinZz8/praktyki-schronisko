from app.model.models import Application, Animal

def get_all_app(request):
    app=Application.objects.all().order_by('-date')
    return app

def get_app_by_id(request, id_app):
    app = Application.objects.get(ID = id_app)
    return app