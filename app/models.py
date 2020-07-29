# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'admin'


class Animal(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    age = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    description = models.TextField()
    entered = models.DateTimeField()
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'animal'

    def __str__(self):
        data = self.name
        return data


class Application(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    info = models.TextField(blank=True, null=True)
    animal = models.ForeignKey(Animal, models.DO_NOTHING)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'application'

class News(models.Model):
    content = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'news'
        verbose_name_plural = 'News'


class Photo(models.Model):
    animal = models.ForeignKey(Animal, models.DO_NOTHING, blank=True, null=True)
    image = models.ImageField(upload_to = 'image', blank=True)
    thumbnail = models.BooleanField(default = False)

    class Meta:
        managed = True
        db_table = 'photo'
