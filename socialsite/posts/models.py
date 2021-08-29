from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from groups.models import Groups
from ckeditor.fields import RichTextField


# Create your models here.

class Posts(models.Model):
    groups_name = models.ForeignKey(Groups, related_name='posts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='my_posts', on_delete=models.CASCADE)
    # post_body = models.TextField(blank=True, null=True)
    post_body = RichTextField(blank=True, null=True)
    post_image = models.ImageField(upload_to='images/posts/', blank=True, null=True)
    post_created = models.DateTimeField(auto_now_add=True)
    post_likes = models.ManyToManyField(User, related_name='post_likes')

    def __str__(self):
        return str(self.groups_name)+ " | "+ str(self.post_body)

    def total_likes(self):
        return self.post_likes.count()

    def total_comments(self):
        return self.comments.count()

    def post_name(self):
        return self.post_body[:100]

    def get_absolute_url(self):
        return reverse("groups:group_detail", kwargs={"slug": self.groups_name.slug})

    class Meta:
        ordering = ["-post_created"]


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userpost')
    body = RichTextField(blank=True, null=True)
    post_img = models.ImageField(blank=True, null=True, upload_to='images/posts/')
    post_like = models.ManyToManyField(User, related_name='userpost_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    def total_likes(self):
        return self.post_like.count()

    class Meta:
        ordering = ["-created_at"]
