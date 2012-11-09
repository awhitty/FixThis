import settings, datetime

from django.db import models

from places.managers import PlaceManager
from places.utils import distance

class Request(models.Model):
	image = models.ImageField(upload_to="images/")
	timestamp = models.DateTimeField(default=datetime.datetime.now())
	description = models.TextField()
	urgency = models.IntegerField()

	# These fields are required by django-places
	latitude = models.DecimalField(max_digits=36, decimal_places=16)
	longitude = models.DecimalField(max_digits=36, decimal_places=16)

	objects = PlaceManager()

	def __unicode__(self):
		return self.description[:20]

	# This function is from django-places as well
	def distance_to(self, *args):
		if len(args) == 2:
			lat, lon = args[0], args[1]
		else:
			lat, lon = args[0].latitude, args[0].longitude
		return distance(self.latitude, self.longitude, lat, lon)