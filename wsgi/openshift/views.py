import os
from django.template import RequestContext
from mappings.models import Mappings
from django.shortcuts import render,render_to_response,redirect,get_object_or_404





def home(request):
	mapping = Mappings()
	shorturl = None
	if request.method=="POST":
		
		mapping.longurl = request.POST.get("longurl")
		mapping.shorturl = mapping.shorten_url(mapping.longurl) 
	
		
		try:
			isLongPresent = Mappings.objects.get(longurl=str(mapping.longurl)).exists()
		except:
			isLongPresent = False
		if isLongPresent is False:
			try:
				isShortPresent = Mappings.objects.get(shorturl=mapping.shorturl).exists()
			except:
				isShortPresent = False
			if isShortPresent is False:
				mapping.clicks = Mappings.objects.get(shorturl=mapping.shorturl).clicks
				mapping.save()
			else:
				while isShortPresent is False:
					mapping.shorturl = mapping.resolve_collision(mapping.longurl)
					try:
        		                        isShortPresent = Mappings.objects.get(shorturl=mapping.shorturl).exists()
	                	        except:
                                		isShortPresent = False

		else:
			mapping.shorturl = Mappings.objects.get(shorturl=mapping.shorturl).shorturl
			mapping.clicks = Mappings.objects.get(shorturl=mapping.shorturl).clicks

	return render_to_response('house/house.html',{"shorturl" : mapping.shorturl, "clicks" : mapping.clicks}, context_instance=RequestContext(request))


def redirecter(request,shortened):
	
	mapping = get_object_or_404(Mappings,shorturl=shortened)
	mapping.clicks +=1
	mapping.save()
	print mapping.clicks
	return redirect(mapping.longurl)
