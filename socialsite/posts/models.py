from django.db import models
from django.contrib.auth.models import User
from groups.models import Groups


# Create your models here.

class Posts(models.Model):
    groups_name = models.ForeignKey(Groups, related_name='posts', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    post_body = models.TextField(blank=True,null=True)
    post_image = models.ImageField(upload_to='images/posts/', blank=True, null=True)
    post_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='posts')

    def __str__(self):
        return self.slug

    def post_name(self):
        return self.post_body[:1000]

    def total_likes(self):
        return self.likes.count()
