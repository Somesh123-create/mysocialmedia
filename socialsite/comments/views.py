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


class AddCommentsView(TemplateView):
    template_name = 'comments/add_comments.html'

    def get_context_data(self, **kwargs):
        all_obj = Comments.objects.all().values()
        context = super().get_context_data(**kwargs)
        return context

class UpdateCommentView(TemplateView):
    template_name = 'comments/update_comments.html'

    def get_context_data(self, **kwargs):
        all_obj = Comments.objects.all().values()
        context = super().get_context_data(**kwargs)
        return context


class DeleteCommentView(TemplateView):
    template_name = 'comments/delete_comments.html'

    def get_context_data(self, **kwargs):
        all_obj = Comments.objects.all().values()
        context = super().get_context_data(**kwargs)
        return context
