from django.db import models
import base64

class Mappings(models.Model):
	shorturl = models.CharField(primary_key=True,max_length=50)
	longurl = models.URLField(max_length=500)
	clicks = models.IntegerField(default=0)

	def __repr__(self):
		return "%s has been hit %s times"%(self.shorturl,self.clicks)

	def shorten_url(self,inputurl):
		length = len(inputurl)
		consturl="tiny-vipassana.rhcloud.com"
		return ""
		
	def resolve_collisions():
		return ""		
