from django.db import models

//komentar


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

class Friend(models.Model):
    friends = models.ForeignKey(User)

class CategoryOfPoi(models.Model):
    category_name = models.CharField(max_length=30)

class Photo(models.Model):
    photo = models.CharField(max_length=30)

class PointOfInterest(models.Model):
    user = models.ForeignKey(User)
    latitude = models.FloatField(max_length=30)
    longitude = models.FloatField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(CategoryOfPoi)
    photos = models.ForeignKey(Photo)




    
# Create your models here.
