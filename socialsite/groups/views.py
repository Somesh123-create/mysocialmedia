from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, RedirectView
from .models import Groups, GroupMember
from posts.models import Posts
from .forms import GroupCreateForm, GroupUpdateForm, GroupPostCreateForm

# Create your views here.

class GroupListView(ListView):
    template_name = 'groups/group_list.html'
    model = Groups
    context_object_name = 'groups'
    ordering = ['-created_date']


class GroupCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Groups
    form_class = GroupCreateForm
    login_url = '/account/login/'
    template_name = 'groups/add_group.html'
    success_message = "%(groups_name)s was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            groups_name=self.object.groups_name,
        )

    def get_object(self):
        return self.request.user


class GroupDetailView(DetailView):
    model = Groups
    context_object_name = 'groups'
    template_name = 'groups/group_details.html'




class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Groups
    form_class = GroupUpdateForm
    login_url = '/account/login/'
    template_name = 'groups/update_group.html'


class Joingroup(LoginRequiredMixin, RedirectView):
    login_url = '/account/login/'

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:group_detail",kwargs={"slug": self.kwargs.get("slug")})


    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Groups,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except:
            messages.warning(self.request,("Warning, already a member of {}".format(group.groups_name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.groups_name))

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, RedirectView):
    login_url = '/account/login/'
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:group_detail",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            memberships = GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get("slug")).get()


        except GroupMember.DoesNotExist:
            messages.warning(self.request,"You can't leave this group because you aren't in it.")

        else:
            memberships.delete()
            messages.success(self.request,"You have successfully left this group.")

        return super().get(request, *args, **kwargs)


class CreateGroupPost(LoginRequiredMixin, CreateView):
    form_class = GroupPostCreateForm
    model = Posts
    login_url = '/account/login/'
    template_name = 'groups/addpost_group.html'


    def form_valid(self, form):
        slug = self.kwargs['slug']
        group_slug = Groups.objects.get(slug=slug)
        self.my_post = form.save(commit=False)
        form.instance.groups_name_id = group_slug.id
        self.my_post.save()
        return super().form_valid(form)
