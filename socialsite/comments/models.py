from django.db import models
from accounts.models import Profile
from posts.models import Posts

# Create your models here.


class Comments(models.Model):
    post_name = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug


class Like(models.Model):
	profile = models.ForeignKey(Profile, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Posts, related_name='likes', on_delete=models.CASCADE)
