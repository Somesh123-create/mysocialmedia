from django.db import models
from accounts.models import Profile

# Create your models here.
class Groups(models.Model):
    profile = models.ForeignKey(Profile, related_name='groups', on_delete=models.CASCADE)
    groups_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100)
    cover_pic = models.ImageField(upload_to='images/groups/', null=True, blank=True)
    type_group = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    about_group = models.CharField(max_length=600)

    def __str__(self):
        return self.groups_name

    def group_tag(self):
        return self.about_group[:50]
