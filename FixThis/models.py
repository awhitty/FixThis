import settings, datetime

from django.db import models

class Location(models.Model):
	lat = models.FloatField()
	lon = models.FloatField()

	def __unicode__(self):
		return "(%s, %s)" % (self.lat, self.lon)

class Request(models.Model):
	image = models.ImageField(upload_to="media/images/")
	timestamp = models.DateTimeField(default=datetime.datetime.now())
	description = models.TextField()
	location = models.ForeignKey(Location)
	urgency = models.IntegerField()

	def __unicode__(self):
		return self.description[:20]