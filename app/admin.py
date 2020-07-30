from django.contrib import admin
from app.model.models import Admin, Animal, Application, News, Photo

# Register your models here.

admin.site.register(Admin)
admin.site.register(Animal)
admin.site.register(Application)
admin.site.register(News)
admin.site.register(Photo)
