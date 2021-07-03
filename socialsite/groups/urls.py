from django.urls import path
from .views import *

urlpatterns = [
    path('group_list/', GroupListView.as_view(), name='group_list'),
]
