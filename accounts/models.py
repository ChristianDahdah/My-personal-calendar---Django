from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    # Rename uploaded profile picture to a more standard one
    def rename_file(self, filename):
        return "photos/{}_{}.jpg".format(self.user_id, self.user.username)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="photos/default.jpg", upload_to=rename_file)

    def __str__(self):
        # Should put first_name field mandatory
        return "{} {}".format(self.user.first_name, self.user.last_name)
