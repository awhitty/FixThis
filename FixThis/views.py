# from django.contrib.gis.geoip import GeoIP

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.views.generic.create_update import update_object

from models import *
from forms import *

# TODO: Consider using another name for requests, since "request" is already a
# thing in Django
def getLocation(request):

	latitude = request.session.get('latitude','')
	longitude = request.session.get('longitude','')
	place = request.session.get('place','')

	if not latitude:
		messages.info(request, "Please set your location, so we can determine what's in your area.")

	return latitude, longitude, place

def home(request, *args, **kwargs):
	if request.user.is_authenticated() or 'skip' in request.session:
		response = RequestContext(request, {
			'request': request,
		})

		if 'skip' in request.session:
			response['login_form'] = SlimAuthenticationForm
			response['registration_form'] = SlimUserCreationForm
		return render_to_response('pages/dashboard.html', response)
	else:
		return redirect('login')

def skipLogin(request, *args, **kwargs):
	request.session['skip'] = True
	return redirect('home')

def setLocation(request, *args, **kwargs):
	lat = request.POST.get('latitude', None)
	lon = request.POST.get('longitude', None)
	place = request.POST.get('place', None)

	next = request.GET.get('next', '/')

	if lat and lon:
		request.session['latitude'] = lat
		request.session['longitude'] = lon
		request.session['place'] = place
		messages.success(request, "Successfully updated your location to %s" % place)

		return redirect(next)

	response = RequestContext(request, {
		'request': request,
		'next': next,
	})

	return render_to_response('pages/location.html', response)

# Taken from django.contrib.auth.views
def login(request, *args, **kwargs):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get('next', '')

    if request.method == "POST":
        form = SlimAuthenticationForm(data=request.POST)
        if form.is_valid():
			auth_login(request, form.get_user())

			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()

			return redirect(redirect_to)
    else:
        form = SlimAuthenticationForm(request)

    request.session.set_test_cookie()

    response = RequestContext(request, {
    	'request': request,
        'login_form': form,
		'registration_form': SlimUserCreationForm
    })

    response.update(csrf(request))
    return render_to_response('pages/login.html', response)

def createUser(request, *args, **kwargs):
	redirect_to = request.REQUEST.get('next', '')

	if request.method == "POST":
		form = SlimUserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			messages.info(request, "Thanks for registering. You are now logged in.")
			new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
			auth_login(request, new_user)
			return redirect('home')

		messages.error(request, "Please fix the errors and try again.")
	else:
		form = SlimAuthenticationForm(request)

	request.session.set_test_cookie()

	response = RequestContext(request, {
    	'request': request,
        'login_form': SlimAuthenticationForm,
		'registration_form': form
    })

	return render_to_response('pages/login.html', response)

def listRequests(request, *args, **kwargs):
	latitude, longitude, place = getLocation(request)

	if latitude and longitude:
		radius = request.GET.get('radius', 2)
		requests = Request.objects.nearby(latitude, longitude, radius)
	else:
		return redirect('location')

	response = RequestContext(request, {
		'request': request, 
		'requests': requests,
		'latitude': latitude,
		'longitude': longitude,
	})

	return render_to_response('pages/list.html', response)

def mapRequests(request, *args, **kwargs):
	latitude, longitude, place = getLocation(request)

	if latitude and longitude:
		radius = request.GET.get('radius', 2)
		requests = Request.objects.nearby(latitude, longitude, radius)
	else:
		return redirect('location')

	response = RequestContext(request, {
		'request': request, 
		'requests': requests,
		'latitude': latitude,
		'longitude': longitude,
	})

	return render_to_response('pages/map.html', response)

def detailRequest(request, request_id, *args, **kwargs):
	latitude, longitude, place = getLocation(request)

	if not latitude and not longitude:
		return redirect('location')

	fixthis_request = get_object_or_404(Request, pk=request_id)



	response = RequestContext(request, {
		'request': request, 
		'fix': fixthis_request,
		'latitude': latitude,
		'longitude': longitude,
	})

	return render_to_response('pages/detail.html', response)

def addRequest(request, *args, **kwargs):
	latitude, longitude, place = getLocation(request)

	back = None

	if not latitude and not longitude:
		return redirect('location')

	if request.method == 'GET':
		form = SubmitForm()
	else:
		# print request.POST
		form = SubmitForm(request.POST, request.FILES)
		print form
		if form.is_valid():
		    req = form.save()
		    if request.user.is_authenticated():
		    	req.submitted_user = request.user

	    		req.save()
	    		return redirect('detail-request', req.id)

		else:
			back = True
			messages.error(request, "Please fix the errors")


	response = RequestContext(request, {
		'request': request,
		'form': form,
		'latitude': latitude,
		'longitude': longitude,
		'place': place,
		'back': back
	})

	response.update(csrf(request))
	return render_to_response('pages/submit.html', response)

def settingsPage(request, *args, **kwargs):
	profile, created = Profile.objects.get_or_create(user=request.user)

	return update_object(request,
                        form_class=ProfileForm,
                        object_id=profile.id,
                        template_name='pages/settings.html')

def updateRequestStatus(request, request_id, *args, **kwargs):
	fixthis_request = get_object_or_404(Request, pk=request_id)
	if request.method == 'POST':
		status = request.POST.get('status','')
		if status == '0':
			fixthis_request.status = 0
			fixthis_request.assigned_user = None
		elif status == '1':
			fixthis_request.status = 1
			fixthis_request.assigned_user = request.user
		else:
			fixthis_request.status = 2
			fixthis_request.assigned_user = None

		print fixthis_request.save()

	return HttpResponse("Success!")

def myfixthis(request, *args, **kwargs):
	profile, created = Profile.objects.get_or_create(user=request.user)
	# subscribed_requests = Request.objects.filter(tags__name__in=profile.subscribed_tags.all())
	subscribed_requests = Request.objects.all()
	submitted_requests = Request.objects.filter(submitted_user=request.user)
	assigned_requests = Request.objects.filter(assigned_user=request.user)

	response = RequestContext(request, {
		'request': request,
		'submitted': submitted_requests,
		'assigned': assigned_requests,
		'subscribed': subscribed_requests,
	})

	return render_to_response('pages/myfixthis.html', response)






		
