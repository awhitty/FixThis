from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'FixThis.views.dashboard', name='home'),
    url(r'^login/$', 'FixThis.views.dashboard', name='login'),
    url(r'^logout/$', 'FixThis.views.dashboard', name='logout'),
    url(r'^register/$', 'FixThis.views.dashboard', name='register'),
    url(r'^settings/$', 'FixThis.views.dashboard', name='settings'),

    url(r'^requests/add/$', 'FixThis.views.dashboard', name='add-request'),
    url(r'^requests/search/$', 'FixThis.views.dashboard', name='search-request'),
    url(r'^requests/detail/(?P<request_id>\d+)/$', 'FixThis.views.dashboard', name='detail-request'),
    url(r'^requests/list/$', 'FixThis.views.listRequests', name='list-requests'),
    url(r'^requests/map/$', 'FixThis.views.dashboard', name='map-requests'),
    url(r'^requests/lookup/(?P<user_id>\d+)/$', 'FixThis.views.dashboard', name='user-requests'),

    # url(r'^FixThis/', include('FixThis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()