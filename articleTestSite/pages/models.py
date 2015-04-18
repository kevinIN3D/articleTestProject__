from django.db import models

class MainPage(models.Model):
	homecopy = models.TextField()

	def __str__(self):
		return 'Home Page Copy'

# Create your models here.
