from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('user_post_list/<slug>', UserPostListView.as_view(), name='user_post_list'),

]


# path('profile/', ProfileView.as_view(), name='profile'),
# path('profile/edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
# path('profile/delete_profile/', ProfileDeleteView.as_view(), name='delete_profile'),
