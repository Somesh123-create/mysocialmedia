from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Profile
from comments.models import Comments
from posts.models import Posts
from .forms import *
# Create your views here.


class UserPostListView(DetailView):
    template_name = 'registration/profile.html'
    model = Profile
    context_object_name = 'my_profile'
    ordering = ['-post_created']


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ChangePasswordView(TemplateView):
    template_name = 'registration/change_password.html'
