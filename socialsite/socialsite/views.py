from django.shortcuts import render
from django.views.generic import ListView
from groups.models import Groups
from posts.models import Posts
from comments.models import Comments


class HomeView(ListView):
    template_name = 'home.html'
    model = Groups
    context_object_name = 'groups'
    ordering = ['-created_date']
