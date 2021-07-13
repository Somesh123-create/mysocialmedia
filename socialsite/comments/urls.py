from django.urls import path

from .views import *

urlpatterns = [

    path('add_comments/', CommentsView.as_view(), name='add_comments'),

]
