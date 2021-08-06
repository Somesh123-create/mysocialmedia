from django.urls import path
from .views import *

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='group_list'),
    path('groups/<slug>', GroupDetailView.as_view(), name='group_detail'),

]
