from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    slug = models.SlugField(max_length=100)
    profile_pic = models.ImageField(upload_to='images/user/profile/', null=True, blank=True)
    cover_pic = models.ImageField(upload_to='images/user/profile/', null=True, blank=True)
    user_bio = models.TextField(null=True,blank=True, max_length=255)
    designation = models.CharField(blank=True,null=True, max_length=255)
    education = models.CharField(blank=True, null=True, max_length=255)
    marital_status = models.CharField(blank=True, null=True, max_length=60)
    hobbies = models.CharField(blank=True, null=True, max_length=500)
    location = models.CharField(blank=True, null=True, max_length=500)
    mobile = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.slug
