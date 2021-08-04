from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('Log_in/', LogInView.as_view(), name='Log_in'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('user_post_list/', UserPostListView.as_view(), name='user_post_list'),

]


# path('profile/', ProfileView.as_view(), name='profile'),
# path('profile/edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
# path('profile/delete_profile/', ProfileDeleteView.as_view(), name='delete_profile'),
