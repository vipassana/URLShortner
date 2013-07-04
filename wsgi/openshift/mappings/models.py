from django.db import models
import base64

charset = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890%"

class Mappings(models.Model):
	shorturl = models.CharField(primary_key=True,max_length=50)
	longurl = models.URLField(max_length=500)
	clicks = models.IntegerField(default=0)

	def __repr__(self):
		return "%s has been hit %s times"%(self.shorturl,self.clicks)

	def shorten_url(self,long_url):
		global charset 

		shortend_url=""
		numprint=0


		short_url_len = len(long_url) / 63
	
		if short_url_len < 3:
			short_url_len = 3
		
		increment = len(long_url) / short_url_len

		for iters in range(0, short_url_len) :

			for index in range(iters, iters+increment):

				numprint+=ord(long_url[index])

			shortend_url += charset[numprint%63]
			numprint = 0
		
		return shortend_url
				
	def resolve_collisions(self, long_url):
		global charset
		numprint = 0
		for iters in len(long_url)-1:
			numprint+=ord(long_url[iters])
		return charset[numprint%63] 		
