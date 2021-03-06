from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from .models import Profile
from comments.models import Comments
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Posts
from .forms import *
# Create your views here.


class UserPostView(DetailView):
    template_name = 'registration/profile.html'
    model = User
    context_object_name = 'my_profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserPostForm()
        return context

class UserPostCreateView(LoginRequiredMixin, CreateView):
    form_class = UserPostForm
    login_url = '/account/login/'
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)




class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ChangePasswordView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('groups:group_list')


class UserSettingsEditView(UpdateView):
    form_class = UserSettingsEditForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('groups:group_list')

    def get_object(self):
        return self.request.user

class UserProfileUpdateView(UpdateView):
    form_class = UserProfileUpdateForm
    template_name = 'registration/profile_update.html'
    model = Profile


class ProfileCreateView(CreateView):
    form_class = UserProfileCreateForm
    model = Profile
    template_name = 'registration/profile_create.html'
