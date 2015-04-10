__author__ = 'Eddie'

# sense_api/api.py

from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization

from sense_api.models import Device
from sense_api.models import TrackRequest
from sense_api.models import LocationLog

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']

class DeviceResource(ModelResource):
    device_owner = fields.ForeignKey(UserResource, 'user', null=True, blank=True)

    class Meta:
        queryset = Device.objects.all()
        resource_name = 'device'
        authorization = Authorization()

class TrackRequestResource(ModelResource):
    user_id = fields.ForeignKey(UserResource, 'user')
    device_id = fields.ForeignKey(DeviceResource, 'device')

    class Meta:
        queryset = TrackRequest.objects.all()
        resource_name = 'trackrequest'
        authorization = Authorization()

class LocationLogResource(ModelResource):
    device_id = fields.ForeignKey(DeviceResource, 'device')

    class Meta:
        queryset = LocationLog.objects.all()
        resource_name = 'locationlog'
        authorization = Authorization()
        filtering = {
            'device_id': ALL,
            'log_time': ALL,
        }
        ordering = [
            'log_time'
        ]