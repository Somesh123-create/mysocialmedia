from django.urls import path
from .views import *
from comments.views import CommentCreateView

app_name = 'posts'

urlpatterns = [
    path('post_feeds/', PostListView.as_view(), name='post_list'),
    path('post_detail/<int:pk>', PostDeatailsView.as_view(), name='post_detail'),
    path('post_detail/<int:pk>/comment_create/', CommentCreateView.as_view(), name='comment_create'),
    path('post_feeds/like/<int:pk>', LikeView.as_view(), name='like_post'),

]
