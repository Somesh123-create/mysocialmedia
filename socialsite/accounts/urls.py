from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('user_settings/', UserSettingsEditView.as_view(), name='user_settings'),
    path('profile/<int:pk>', UserPostView.as_view(), name='user_post_list'),
    path('user_post_list/<int:pk>/edit_profile', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('create_profile/', ProfileCreateView.as_view(), name='create_profile'),

]

# path('profile/', ProfileView.as_view(), name='profile'),
# path('profile/edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
# path('profile/delete_profile/', ProfileDeleteView.as_view(), name='delete_profile'),
