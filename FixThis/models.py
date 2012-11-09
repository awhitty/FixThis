import settings, datetime

from django.db import models
from django.contrib.auth.models import User

from places.managers import PlaceManager
from places.utils import distance

from taggit.managers import TaggableManager

class Request(models.Model):
	image = models.ImageField(upload_to="images/")
	timestamp = models.DateTimeField(default=datetime.datetime.now())
	description = models.TextField()
	urgency = models.IntegerField()

	ORDER_STATUS = ((0, 'Open'), (1, 'Taken'), (2, 'Done'))
	status = models.SmallIntegerField(default=0, choices=ORDER_STATUS)
	assigned_user = models.ForeignKey(User, blank=True, null=True, related_name="ftrequest_assigned")
	submitted_user = models.ForeignKey(User, blank=True, null=True, related_name="ftrequest_submitted")

	# These fields are required by django-places
	latitude = models.DecimalField(max_digits=36, decimal_places=16)
	longitude = models.DecimalField(max_digits=36, decimal_places=16)

	objects = PlaceManager()
	tags = TaggableManager()

	def __unicode__(self):
		return self.description[:20]

	# This function is from django-places as well
	def distance_to(self, *args):
		if len(args) == 2:
			lat, lon = args[0], args[1]
		else:
			lat, lon = args[0].latitude, args[0].longitude
		return distance(self.latitude, self.longitude, lat, lon)

class Profile(models.Model):
	# default location?
	user = models.ForeignKey(User, unique=True, default=0)
	subscribed_tags = TaggableManager()