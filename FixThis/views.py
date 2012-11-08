# from django.contrib.gis.geoip import GeoIP

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib import messages

from models import *
from forms import *

# TODO: Consider using another name for requests, since "request" is already a
# thing in Django

def dashboard(request):
	return render_to_response('pages/dashboard.html')

def listRequests(request):
	try:
		latitude = request.COOKIES['userLat']
		longitude = request.COOKIES['userLon']
	except:
		# this is where we could try to find the user's location by IP address
		latitude = 30
		longitude = 30

	if latitude:
		requests = Request.objects.nearby(latitude, longitude, 2)
	else:
		requests = Request.objects.all()

	response = {
		'request': request, 
		'requests': requests,
		'latitude': latitude,
		'longitude': longitude,
	}

	return render_to_response('pages/list.html', response)

def mapRequests(request):
	requests = Request.objects.all()

	response = {
		'request': request, 
		'requests': requests,
		# 'latitude': lat,
		# 'longitude': lon
	}

	return render_to_response('pages/map.html', response)

def detailRequest(request, request_id):
	try:
		latitude = request.COOKIES['userLat']
		longitude = request.COOKIES['userLon']
	except:
		latitude = 30
		longitude = 30

	fixthis_request = get_object_or_404(Request, pk=request_id)

	response = {
		'request': request, 
		'fix': fixthis_request,
		'latitude': latitude,
		'longitude': longitude,
	}

	return render_to_response('pages/detail.html', response)

def addRequest(request):
	if request.method == 'GET':
		form = SubmitForm()
	else:
		print request.FILES
		form = SubmitForm(request.POST, request.FILES)
		if form.is_valid():
		    form.save()
		    try:
		    	return redirect(request.GET['next'])
		    except:
		    	redirect('home')
		else:
			messages.error(request, "Please fix the errors")


	response = {
		'request': request,
		'form': form,
	}

	response.update(csrf(request))
	return render_to_response('pages/submit.html', response)

def previewImage(request):
	if request.method == 'POST':
		print request.POST
		return HttpResponse("Good request")
	else:
		return "Bad request!"











		