from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, CreateView, RedirectView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Posts, UserPost
from django.contrib.auth.mixins import LoginRequiredMixin
from groups.models import Groups
from comments.models import Comments
from .forms import PostCreateForm
from braces.views import SelectRelatedMixin
from django.http import HttpResponseRedirect
import datetime
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy, reverse
from comments.forms import CommentCreateForm, CommentReplyForm
from groups.forms import GroupPostCreateForm
from accounts.forms import UserPostForm
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
        context['commreply_form'] = CommentReplyForm()
        context['userpostform'] = UserPostForm()
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

class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = GroupPostCreateForm
    model = Posts
    login_url = '/account/login/'
    template_name = 'posts/update_post.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Posts
    login_url = '/account/login/'
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('posts:post_list')


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

class UserPostLikeView(LoginRequiredMixin, RedirectView):
    login_url = '/account/login/'


    def get(self, request, *args, **kwargs):
        post = get_object_or_404(UserPost, id=request.POST.get("post_id"))
        liked = False
        if post.post_like.filter(id=request.user.id).exists():
            post.post_like.remove(request.user)
            liked = False
        else:
            post.post_like.add(request.user)
            liked = True
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse("posts:post_list")
