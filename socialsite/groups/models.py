from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Groups(models.Model):
    user = models.ForeignKey(User, related_name='user_group', on_delete=models.CASCADE)
    groups_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    cover_pic = models.ImageField(upload_to='images/groups/', null=True, blank=True)
    type_group = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    about_group = models.TextField(max_length=600)
    members = models.ManyToManyField(User,through="GroupMember", related_name='all_group_memb')

    def __str__(self):
        return self.groups_name

    def group_tag(self):
        return self.about_group[:50]

    def total_members(self):
        return self.members.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.groups_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:group_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["groups_name"]



class GroupMember(models.Model):
    group = models.ForeignKey(Groups, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


    class Meta:
        unique_together = ("group", "user")
