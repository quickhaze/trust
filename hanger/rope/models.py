from django.db import models

# Create your models here.

class Cow(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	unit = models.ForeignKey(
		'Milk',
		on_delete= models.CASCADE
		)


class Milk(models.Model):
	color = models.CharField(max_length=20)
	capacity= models.IntegerField()
