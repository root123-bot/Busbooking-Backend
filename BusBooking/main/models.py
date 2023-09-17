from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class DeviceAuthModel(models.Model):
    modelId = models.CharField(max_length=255)
    pin = models.CharField(max_length=255)


class DeviceNotificationToken(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="notificationToken")
    deviceNotificationToken = models.CharField(max_length=255)
