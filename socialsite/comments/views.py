from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Comments
import datetime
# Create your views here.

class CommentListView(ListView):
    model = Comments
    template_name = 'comments/comments_list.html'
    context_object_name = 'comments'
    ordering = ['-date_created']
