from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gis_models
from libraries.models import Store

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_location = gis_models.PointField(null=True, blank=True)
    last_ip_address = models.GenericIPAddressField(null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
