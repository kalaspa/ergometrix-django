from django.db import models

# Create your models here.

class Rower (models.Model):

	lastname = models.CharField(max_length=50)
	firstname = models.CharField(max_length=50)
	birthdate = models.DateField()
	license = models.CharField(max_length=50)

	def __str__(self):
		return "{0} {1} né(e) le {2}, no de license {3}".format(self.lastname , self.firstname , self.birthdate , self.license)

class Leader (models.Model):

	email = models.EmailField()
	phone = models.IntegerField()
	club = models.CharField(max_length=50)
	rower = models.ForeignKey(Rower)

	def __str__(self):
		return "{0}, {1} {2} du club {3}".format(self.rower , self.email , self.phone , self.club)

class Category (models.Model):

	code = models.CharField(max_length=50)
	description = models.CharField(max_length=100)

	def __str__(self):
		return "{0} {1}".format(self.code , self.description)

class Boat (models.Model):

	name = models.CharField(max_length=50)
	record = models.IntegerField(null=False)

	payment = models.BooleanField()
	deleted = models.BooleanField()
	valid = models.BooleanField()
	created = models.DateField()

	rower = models.ManyToManyField(Rower)
	leader = models.ForeignKey(Leader)
	category = models.ForeignKey(Category)

	def __str__(self):
		return "{0} {1} ".format(self.name , self.category)