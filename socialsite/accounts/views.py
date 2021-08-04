from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Profile
from comments.models import Comments
from posts.models import Posts
# Create your views here.


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class LogInView(TemplateView):
    template_name = 'registration/login.html'


class ChangePasswordView(TemplateView):
    template_name = 'registration/change_password.html'


class UserPostListView(ListView):
    template_name = 'registration/profile.html'
    model = Posts
    context_object_name = 'posts'
    ordering = ['-post_created']

    def get_context_data(self, **kwargs):
        all_comments = Comments.objects.all()
        context = super().get_context_data(**kwargs)
        context['comments'] = all_comments
        return context
