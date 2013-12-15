from django.db import models
from django import forms

class User(models.Model):
<<<<<<< HEAD
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    friends = models.ForeignKey('self', blank=True, default='null',on_delete=models.SET_DEFAULT);

=======
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=50)
	nickname = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=30)

class Friend(models.Model):
	friends = models.ForeignKey(User)
>>>>>>> 327913c346d6ee17b434c878952817f8e2b41515

class CategoryOfPoi(models.Model):
	category_name = models.CharField(max_length=30)

class Photo(models.Model):
	title = models.CharField(max_length=30)

class PointOfInterest(models.Model):
	user = models.ForeignKey(User)
	latitude = models.FloatField(max_length=30)
	longitude = models.FloatField(max_length=30)
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	category = models.ForeignKey(CategoryOfPoi)
	photos = models.ForeignKey(Photo)


class CreatePoi(forms.Form):
	title = forms.CharField(required=True, max_length=100, initial="")
	description = forms.CharField(required=True, widget=forms.Textarea, initial="")
	latitude = forms.CharField(widget=forms.HiddenInput)
	longitude = forms.CharField(widget=forms.HiddenInput)

class Login(forms.Form):
	username = forms.CharField(required=True, max_length=30, initial="")
	password = forms.CharField(max_length=32, widget=forms.PasswordInput, initial="")
	#widget=forms.HiddenInput



# Create your models here.
