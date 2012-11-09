from django import template

from ..utils import distance

register = template.Library()

@register.inclusion_tag('includes/distance_format.html')
def distance_to(a_lat, a_lon, b_lat, b_lon):
    return {'distance': (distance(float(a_lat), float(a_lon), float(b_lat), float(b_lon)))}