from django.contrib import admin
from .models import Comments, Like, CommentReply


admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(CommentReply)
