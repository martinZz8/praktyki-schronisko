from app.model.models import Animal, Application, News, Photo
from django.forms import ModelForm
from django import forms
import datetime

# class AdminCreate (forms.ModelForm):
#     class Meta:
#         model = Admin
#         fields = '__all__'


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
        model = News
        fields = ('title', 'content', 'image', 'visible')
        labels = {
            "title": "Tytuł",
            "content": "Treść",
            "image": "Zdjęcie",
            "visible": "Widoczność posta dla odwiedzających."
        }


ANIMAL_TYPE_CHOICES = (
    ('Pies', 'pies'),
    ('Kot', 'kot')
)

ANIMAL_SEX_CHOICES = (
    ('Samiec', 'samiec'),
    ('Samica', 'samica')
)

current_year = datetime.datetime.now().year


class Animal_Create(forms.ModelForm):

    entered = forms.DateField(
        widget=forms.SelectDateWidget(years=range(
            current_year - 2, current_year + 1)),
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
        model = Animal
        fields = ('name', 'age', 'sex', 'description',
                  'entered', 'type', 'race')
        labels = {
            "name": "Imię",
            "age": "Wiek",
            "description": "Opis",
            "race": "Rasa"
        }


class Photo_create(forms.Form):
    img = forms.ImageField()


class Application_Create(forms.Form):
    name = forms.CharField(max_length=20, label="Imię",
                           widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    surname = forms.CharField(max_length=30, label="Nazwisko", widget=forms.TextInput(
        attrs={'placeholder': 'Nazwisko'}))
    email = forms.CharField(max_length=40, label="Adres e-mail",
                            widget=forms.TextInput(attrs={'placeholder': 'Adres e-mail'}))
    info = forms.CharField(label="Dlaczego chcesz przygarnąć tego zwierzaka?", widget=forms.Textarea(
        attrs={'placeholder': 'Dlaczego chcesz przygarnąć tego zwierzaka?'}))
