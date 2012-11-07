from django import template

from ..utils import distance

register = template.Library()

def distance_to(a_lat, a_lon, b_lat, b_lon):
    return distance(float(a_lat), float(a_lon), float(b_lat), float(b_lon))

register.simple_tag(distance_to)