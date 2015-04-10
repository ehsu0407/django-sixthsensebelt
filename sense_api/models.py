from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):
    device_name = models.CharField(max_length=256)
    device_owner = models.ForeignKey(User)

class TrackRequest(models.Model):
    user_id = models.ForeignKey(User)
    device_id = models.ForeignKey(Device)
    status = models.CharField(max_length=256, default='Pending')

class LocationLog(models.Model):
    device = models.ForeignKey(Device)
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
    log_time = models.DateTimeField(auto_now_add=True)