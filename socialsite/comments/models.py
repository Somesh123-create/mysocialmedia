from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts

# Create your models here.


class Comments(models.Model):
    post_name = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    comment_likes = models.ManyToManyField(User, related_name='comments')

    def __str__(self):
        return self.slug
