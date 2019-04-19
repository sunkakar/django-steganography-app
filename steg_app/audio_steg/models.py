from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    stegtype = models.CharField(max_length=20)
    hiddentext = models.TextField(max_length=60)
    date = models.DateTimeField(default=timezone.now)
    stegtext = models.CharField(max_length=300)
    stegimage = models.ImageField(default='default.jpeg',upload_to='steg_image')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.stegtype

