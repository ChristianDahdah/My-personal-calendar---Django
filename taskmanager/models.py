from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #must add groups and avatar later

    def __str__(self):
        # Should put first_name field mandatory
        return "Profile de {0}".format(self.user.first_name)
