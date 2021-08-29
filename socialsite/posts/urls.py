from django.urls import path
from .views import *
from comments.views import CommentCreateView

app_name = 'posts'

urlpatterns = [
    path('post_feeds/', PostListView.as_view(), name='post_list'),
    path('post_feeds/<int:pk>/update_post/', PostUpdateView.as_view(), name='update_post'),
    path('post_feeds/<int:pk>/delete_post', PostDeleteView.as_view(), name='delete_post'),
    path('post_detail/<int:pk>', PostDeatailsView.as_view(), name='post_detail'),
    path('post_detail/<int:pk>/comment_create/', CommentCreateView.as_view(), name='comment_create'),
    path('post_feeds/like/<int:pk>', LikeView.as_view(), name='like_post'),
    path('user_postlike/<int:pk>', UserPostLikeView.as_view(), name='user_postlike'),

]
