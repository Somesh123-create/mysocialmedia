from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Comments
import datetime
from posts.models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentCreateForm
# Create your views here.

class CommentListView(ListView):
    model = Comments
    template_name = 'comments/comments_list.html'
    context_object_name = 'comments'
    ordering = ['-date_created']

class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentCreateForm
    login_url = '/account/login/'
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        post_name = Posts.objects.get(pk=pk)
        form.instance.user = self.request.user
        form.instance.post_name_id = post_name.id
        form.save()
        return super().form_valid(form)
