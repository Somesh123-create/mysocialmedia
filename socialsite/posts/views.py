from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, CreateView, RedirectView, DetailView
from django.urls import reverse
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin
from groups.models import Groups
from comments.models import Comments
from .forms import PostCreateForm
from braces.views import SelectRelatedMixin
from django.http import HttpResponseRedirect
import datetime
from comments.forms import CommentCreateForm

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
        context['form'] = CommentCreateForm()
        return context


class PostDeatailsView(DetailView):
    model = Posts
    context_object_name = 'post'
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        all_groups = Groups.objects.all()
        context = super().get_context_data(**kwargs)
        context['form'] = CommentCreateForm()
        return context




class LikeView(LoginRequiredMixin, RedirectView):
    login_url = '/account/login/'


    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Posts, id=request.POST.get("post_id"))
        liked = False
        if post.post_likes.filter(id=request.user.id).exists():
            post.post_likes.remove(request.user)
            liked = False
        else:
            post.post_likes.add(request.user)
            liked = True
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse("posts:post_detail", kwargs={"pk": self.kwargs.get("pk")})
