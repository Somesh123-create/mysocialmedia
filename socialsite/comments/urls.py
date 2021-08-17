from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('comments_list/', CommentListView.as_view(), name='comments_list'),



]
