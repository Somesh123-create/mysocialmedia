from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('comments_list/', CommentListView.as_view(), name='comments_list'),
    path('add_comments/', AddCommentsView.as_view(), name='add_comments'),
    path('update_comments/', UpdateCommentView.as_view(), name='update_comments'),
    path('delete_comments/', DeleteCommentView.as_view(), name='delete_comments'),

]
