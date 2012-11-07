import settings

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
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

    # Submitting a request
    url(r'^requests/add/$', 'FixThis.views.addRequest', name='add-request'),
    url(r'^requests/preview/$', 'FixThis.views.previewImage', name='preview-image'),


    url(r'^requests/search/$', 'FixThis.views.dashboard', name='search-request'),
    url(r'^requests/detail/(?P<request_id>\d+)/$', 'FixThis.views.detailRequest', name='detail-request'),
    url(r'^requests/list/$', 'FixThis.views.listRequests', name='list-requests'),
    url(r'^requests/map/$', 'FixThis.views.mapRequests', name='map-requests'),
    url(r'^requests/lookup/(?P<user_id>\d+)/$', 'FixThis.views.dashboard', name='user-requests'),

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