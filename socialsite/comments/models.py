from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from posts.models import Posts

# Create your models here.


class Comments(models.Model):
    post_name = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + '|' + self.body

    class Meta:
        ordering = ["-date_created"]

    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"pk": self.post_name.pk})



class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Posts, related_name='likes', on_delete=models.CASCADE)
