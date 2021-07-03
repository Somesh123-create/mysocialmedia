from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PostListView(TemplateView):
    template_name = 'post_list.html'
