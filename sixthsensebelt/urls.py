from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from sense_api.api import *

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(DeviceResource())
v1_api.register(TrackRequestResource())
v1_api.register(LocationLogResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sixthsensebelt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
