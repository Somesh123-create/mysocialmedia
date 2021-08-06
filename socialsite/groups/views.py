from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Groups

# Create your views here.

class GroupListView(ListView):
    template_name = 'groups/group_list.html'
    model = Groups
    context_object_name = 'groups'
    ordering = ['-created_date']

class GroupDetailView(DetailView):
    model = Groups
    context_object_name = 'groups'
    template_name = 'groups/group_details.html'
