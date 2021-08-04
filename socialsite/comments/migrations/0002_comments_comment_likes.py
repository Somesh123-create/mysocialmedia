# Generated by Django 3.2.5 on 2021-08-04 20:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_likes',
            field=models.ManyToManyField(related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
