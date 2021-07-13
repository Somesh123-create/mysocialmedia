from django.db import models

# Create your models here.

class Comments(models.Model):
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
