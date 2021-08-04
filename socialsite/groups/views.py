from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Groups
from posts.models import Posts
from comments.models import Comments
import datetime

# Create your views here.

class GroupPostView(ListView):
    template_name = 'groups/group_posts.html'
    model = Posts
    context_object_name = 'posts'
    ordering = ['-post_created']

    def get_context_data(self, **kwargs):
        all_comments = Comments.objects.all()
        context = super().get_context_data(**kwargs)
        context['comments'] = all_comments
        return context
