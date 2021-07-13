from django.db import models

# Create your models here.

class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    post_body = models.TextField(blank=True,null=True)
    post_image = models.ImageField(blank=True, null=True)
    post_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
