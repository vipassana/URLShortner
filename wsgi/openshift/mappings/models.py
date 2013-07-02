from django.db import models

class Mappings(models.Model):
	shorturl = models.CharField(primary_key=True,max_length=50)
	longurl = models.CharField(max_length=500)
	clicks = models.IntegerField()
