import os
from django.template import RequestContext
from mappings.models import Mappings
from django.http import HttpResponse
from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from httplib import HTTPConnection
import urllib2


counter=0

def home(request):
	shorturl = None
	if request.method=="POST":
		mapping = Mappings()
		mapping.longurl = request.POST.get("longurl")
		global counter 
		counter += 13
		mapping.shorturl = str(counter)
		mapping.clicks=0
		mapping.save()
		shorturl = mapping.shorturl
	return render_to_response('house/house.html',{"shorturl" : shorturl}, context_instance=RequestContext(request))

def redirecter(request,shortened):
#	thisone = Mappings.objects.filter(shorturl='ASDF')
#	return redirect(thisone.longurl)
	mapping = get_object_or_404(Mappings,shorturl=shortened)
	print mapping.longurl
	return redirect(mapping.longurl)
