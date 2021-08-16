from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from groups.models import Groups


# Create your models here.

class Posts(models.Model):
    groups_name = models.ForeignKey(Groups, related_name='posts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='my_posts', on_delete=models.CASCADE)
    post_body = models.TextField(blank=True,null=True)
    post_image = models.ImageField(upload_to='images/posts/', blank=True, null=True)
    post_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' |' + str(self.groups_name)

    def post_name(self):
        return self.post_body[:1000]

    def get_absolute_url(self):
        return reverse("groups:group_detail", kwargs={"slug": self.groups_name.slug})

    class Meta:
        ordering = ["-post_created"]
