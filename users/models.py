from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reward_points = models.PositiveIntegerField(default=0)
    membership_tier = models.CharField(max_length=20,
                                       default='Bronze')

    def __str__(self):
        return self.user.username
