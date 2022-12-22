from PIL import Image
from decouple import config
from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User

S3_URL = config('S3_URL', default='')


class ColourSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color_primary = ColorField(default='#DFD9D6')
    color_accent = ColorField(default='#DBC2D1')
    color_background = ColorField(default='#0A0A0A')
    mask_opacity = models.FloatField(default=0.7, max_length=1)

    def __str__(self):
        return self.user.username + '\'s colour settings'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', default='/avatar/default.png')
    avatar_s3_url = models.URLField(default=S3_URL + '/avatar/pfp.png')

    def __str__(self):
        return self.user.username + '\'s profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 256 or img.width > 256:
                output_size = (256, 256)
                img.thumbnail(output_size)
                img.save(self.avatar.path)


class SignUpRequest(models.Model):
    username = models.CharField(max_length=255)
    osu_user_id = models.IntegerField(default=0)
    authentication_key = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.username + '\'s sign up request'