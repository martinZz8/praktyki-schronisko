from .models import Admin, Animal, Application, News, Photo
from django.forms import ModelForm
from django import forms

class AdminCreate (forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

class AnimalCreate (forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class ApplicationCreate (forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

class NewsCreate (forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class PhotoCreate (forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class New_Create(forms.ModelForm):
     class Meta:
         model=News
         fields=('content','date')