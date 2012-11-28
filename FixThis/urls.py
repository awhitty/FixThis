import settings

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'FixThis.views.home', name='home'),
    url(r'^login/$', 'FixThis.views.login', {'template': 'pages/login.html'}, name='login'),
    url(r'^login/b/$', 'FixThis.views.login', {'template': 'pages/login_b.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^register/$', 'FixThis.views.createUser', name='register'),
    
    url(r'^skip/$', 'FixThis.views.skipLogin', name='skip'),

    url(r'^settings/$', 'FixThis.views.settingsPage', name='settings'),
    url(r'^myfixthis/$', 'FixThis.views.myfixthis', name='myfixthis'),

    url(r'^location/$', 'FixThis.views.setLocation', name='location'),

    # Submitting a request
    url(r'^requests/add/$', 'FixThis.views.addRequest', name='add-request'),

    url(r'^requests/search/$', 'FixThis.views.home', name='search-request'),
    url(r'^requests/detail/(?P<request_id>\d+)/$', 'FixThis.views.detailRequest', name='detail-request'),
    url(r'^requests/list/$', 'FixThis.views.listRequests', name='list-requests'),
    url(r'^requests/map/$', 'FixThis.views.mapRequests', name='map-requests'),
    url(r'^requests/lookup/(?P<user_id>\d+)/$', 'FixThis.views.home', name='user-requests'),
    url(r'^requests/assign/(?P<request_id>\d+)/$', 'FixThis.views.updateRequestStatus', name='update-request'),

    # url(r'^FixThis/', include('FixThis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     urlpatterns += patterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#             'show_indexes': True
#         }),
#    )
