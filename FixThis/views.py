# from django.contrib.gis.geoip import GeoIP

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.views.generic.create_update import update_object

from models import *
from forms import *

# TODO: Consider using another name for requests, since "request" is already a
# thing in Django

def home(request):

	if request.user.is_authenticated() or 'skip' in request.session:
		response = {
			'request': request,
		}

		if 'skip' in request.session:
			response['login_form'] = SlimAuthenticationForm
			response['registration_form'] = SlimUserCreationForm
		return render_to_response('pages/dashboard.html', response)
	else:
		return redirect('login')

def skipLogin(request):
	request.session['skip'] = True
	return redirect('home')

# Taken from django.contrib.auth.views
def login(request):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get('next', '')

    if request.method == "POST":
        form = SlimAuthenticationForm(data=request.POST)
        if form.is_valid():
			print "valid!"
            # # Use default setting if redirect_to is empty
            # # Heavier security check -- don't allow redirection to a different
            # # host.
            # if netloc and netloc != request.get_host():
            #     redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security checks complete. Log the user in.
			auth_login(request, form.get_user())

			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()

			return redirect(redirect_to)
    else:
        form = SlimAuthenticationForm(request)

    request.session.set_test_cookie()

    response = {
    	'request': request,
        'login_form': form,
		'registration_form': SlimUserCreationForm
    }

    response.update(csrf(request))
    return render_to_response('pages/login.html', response)

def createUser(request):
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

	else:
		form = SlimAuthenticationForm(request)

	request.session.set_test_cookie()

	response = {
    	'request': request,
        'login_form': SlimAuthenticationForm,
		'registration_form': form
    }

	return render_to_response('pages/login.html', response)

def listRequests(request):
	try:
		latitude = request.COOKIES['userLat']
		longitude = request.COOKIES['userLon']
	except:
		# this is where we could try to find the user's location by IP address
		# or last known location? privacy setting for this would be good too
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
	try:
		latitude = request.COOKIES.get('userLat', '')
		longitude = request.COOKIES.get('userLon', '')
	except:
		pass

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
		form = SubmitForm(request.POST, request.FILES)
		if form.is_valid():
		    req = form.save()
		    if request.user.is_authenticated():
		    	req.submitted_user = request.user
		    	req.save()

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

		return HttpResponse("Good request")
	else:
		return "Bad request!"

# @login_required
def settingsPage(request):
	profile, created = Profile.objects.get_or_create(user=request.user)

	return update_object(request,
                        form_class=ProfileForm,
                        object_id=profile.id,
                        template_name='pages/settings.html')

def updateRequestStatus(request, request_id):
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

def myfixthis(request):
	submitted_requests = Request.objects.filter(submitted_user=request.user)
	assigned_requests = Request.objects.filter(assigned_user=request.user)

	response = {
		'request': request,
		'submitted': submitted_requests,
		'assigned': assigned_requests,
	}

	return render_to_response('pages/myfixthis.html', response)






		
