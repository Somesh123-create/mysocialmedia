from django.db import models

# Create your models here.
class Groups(models.Model):
    groups_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100)
    cover_pic = models.ImageField(null=True, blank=True)
    type_group = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    about_group = models.CharField(max_length=600)

    def __str__(self):
        return self.groups_name
