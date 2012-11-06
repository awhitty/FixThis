# from django.contrib.gis.geoip import GeoIP
from django.shortcuts import render_to_response, get_object_or_404

from models import *

# TODO: Consider using another name for requests, since "request" is already a
# thing in Django

def dashboard(request):
	return render_to_response('pages/dashboard.html')

def listRequests(request):
	requests = Request.objects.all()

	response = {
		'request': request, 
		'requests': requests
	}

	return render_to_response('pages/list.html', response)

def mapRequests(request):
	requests = Request.objects.all()

	# Get user's latitude and longitude from IP address (for default map centering) 
	# FIXME: We need to set up GeoIP like
	# https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoip/
	# g = GeoIP()
 	# client_ip = request.META['REMOTE_ADDR']
 	# lat, lon = g.lat_lon(client_ip)

	response = {
		'request': request, 
		'requests': requests,
		# 'latitude': lat,
		# 'longitude': lon
	}

	return render_to_response('pages/map.html', response)

def detailRequest(request, request_id):
	print request_id
	fixthis_request = get_object_or_404(Request, pk=request_id)

	response = {
		'request': request, 
		'fix': fixthis_request
	}

	return render_to_response('pages/detail.html', response)

def addRequest(request):
	if request.method == 'GET':
		return render_to_response('pages/submit.html')
	elif request.method == 'POST':
		# process the request submission
		return "posted!"

	return "Bad request"