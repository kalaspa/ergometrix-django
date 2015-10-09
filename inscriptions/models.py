from django.db import models

# Create your models here.

class Rower (models.Model):

	lastname = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)
	birthdate = models.DateField()
	license = models.CharField(max_length=50)

class Leader (models.Model):

	email = models.EmailField()
	phone = models.IntegerField()
	club = models.CharField(max_length=50)

class Category (models.Model):

	code = models.CharField(max_length=50)
	description = models.CharField(max_length=100)

class Boat (models.Model):

	name = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	record = models.IntegerField()

	payment = models.BooleanField()
	deleted = models.BooleanField()
	valid = models.BooleanField()
	created = models.DateField()

	rower = models.ManyToManyField(Rower)
	leader = models.ManyToManyField(Leader)