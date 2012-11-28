from django.shortcuts import redirect
from django.contrib import messages

from models import Profile

class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

class EnsureLocation(object):
	def process_view(self, request, view_func, view_args, view_kwargs):
		lat = request.session.get('latitude', None)
		lon = request.session.get('longitude', None)

		if not lat and not lon:
			messages.add_message(request, messages.INFO, "Please provide a default location.")
			return redirect('location')