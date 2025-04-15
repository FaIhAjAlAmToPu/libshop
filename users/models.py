from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gis_models
from libraries.models import Store

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_location = gis_models.PointField()
    last_ip_address = models.GenericIPAddressField()
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)
    staff_role = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username
