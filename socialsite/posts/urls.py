from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('post_feeds/', PostListView.as_view(), name='post_list'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),

]
