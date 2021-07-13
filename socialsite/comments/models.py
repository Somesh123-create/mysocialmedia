from django.db import models

# Create your models here.


class Comments(models.Model):
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
