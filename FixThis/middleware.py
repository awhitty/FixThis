class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

class AttachLocation(object):
	def process_view(self, request, view_func, view_args, view_kwargs):
		# print request
		print view_func
		latitude = request.COOKIES.get('userLat','')
		longitude = request.COOKIES.get('userLon','')

		view_kwargs['latitude'] = latitude
		view_kwargs['longitude'] = longitude