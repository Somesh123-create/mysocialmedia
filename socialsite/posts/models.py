from django.db import models
from groups.models import Groups
from accounts.models import Profile


# Create your models here.

class Posts(models.Model):
    groups_name = models.ForeignKey(Groups, related_name='posts', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='my_posts', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    post_body = models.TextField(blank=True,null=True)
    post_image = models.ImageField(upload_to='images/posts/', blank=True, null=True)
    post_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    def post_name(self):
        return self.post_body[:1000]
