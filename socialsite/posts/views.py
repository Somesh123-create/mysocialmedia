from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Posts
from groups.models import Groups
from comments.models import Comments
import datetime

# Create your views here.

class PostListView(ListView):
    template_name = 'posts/post_list.html'
    model = Posts
    context_object_name = 'posts'
    ordering = ['-post_created']

    def get_context_data(self, **kwargs):
        all_groups = Groups.objects.all()
        context = super().get_context_data(**kwargs)
        context['groups'] = all_groups
        return context
