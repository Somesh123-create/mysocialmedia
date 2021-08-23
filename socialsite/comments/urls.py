from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('comments_list/', CommentListView.as_view(), name='comments_list'),
    path('<int:pk>/comments_edit/', CommentEditView.as_view(), name='comments_edit'),
    path('<int:pk>/comments_delete/', CommentDeleteView.as_view(), name='comments_delete'),
    path('comment_reply/', CommentReplayView.as_view(), name='comment_reply'),


]
