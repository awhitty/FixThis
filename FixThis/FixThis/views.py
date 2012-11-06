from django.shortcuts import render_to_response

from models import *

def dashboard(request):
	return render_to_response('pages/dashboard.html')

def listRequests(request):
	requests = Request.objects.all()

	response = {
		'request': request, 
		'requests': requests
	}

	return render_to_response('pages/list.html', response)