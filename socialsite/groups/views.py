from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class GroupListView(TemplateView):
    template_name = 'group_list.html'
