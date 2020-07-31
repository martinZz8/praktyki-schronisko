from app.model.models import Admin, Animal, Application, News, Photo
from django.forms import ModelForm
from django import forms
import datetime

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
         fields=( 'title', 'content')
         labels = {
             "title": "Tytuł",
             "content": "Treść"
         }

ANIMAL_TYPE_CHOICES = (
    ('Pies', 'pies'), 
    ('Kot', 'kot')
)

ANIMAL_SEX_CHOICES = (
    ('Samiec', 'samiec'),
    ('Samica', 'samica')
)

class Animal_Create(forms.ModelForm):

    entered = forms.DateField(  
        widget=forms.SelectDateWidget,
        initial=datetime.date.today,
        label="Data przybycia"
    )

    type = forms.ChoiceField(
        required=False,
        choices=ANIMAL_TYPE_CHOICES,
        label="Rodzaj"
    )

    sex = forms.ChoiceField(
        required=False,
        choices=ANIMAL_SEX_CHOICES,
        label="Płeć"
    )

    class Meta:
        model=Animal
        fields=( 'name', 'age', 'sex', 'description', 'entered', 'type', 'race')
        labels = {
          "name": "Imię",
          "age": "Wiek",
          "description": "Opis",
          "race": "Rasa"
         }