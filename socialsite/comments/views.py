from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class CommentsView(TemplateView):
    template_name = 'comments/add_comments.html'
