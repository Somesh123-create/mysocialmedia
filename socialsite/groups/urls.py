from django.urls import path
from .views import *

app_name = 'groups'

urlpatterns = [
    path('group_posts/', GroupPostView.as_view(), name='group_posts'),

]
