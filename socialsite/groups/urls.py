from django.urls import path
from .views import *

app_name = 'groups'

urlpatterns = [
    path('', GroupListView.as_view(), name='group_list'),
    path('create_group/', GroupCreateView.as_view(), name='create_group'),
    path('group_detail/<slug>', GroupDetailView.as_view(), name='group_detail'),
    path('group_detail/<slug>/create_grouppost/', CreateGroupPost.as_view(), name='create_grouppost'),
    path('group_update/<slug>', GroupUpdateView.as_view(), name='group_update'),
    path('join/<slug>/', Joingroup.as_view(), name='join_group'),
    path('leave/<slug>/', LeaveGroup.as_view(), name='leave_group'),

]
