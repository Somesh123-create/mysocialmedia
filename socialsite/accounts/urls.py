from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('user_settings/', UserSettingsEditView.as_view(), name='user_settings'),
    path('profile/<int:pk>', UserPostView.as_view(), name='user_post_list'),
    path('createuser_post/', UserPostCreateView.as_view(), name='createuser_post'),
    path('user_post_list/<int:pk>/edit_profile', UserProfileUpdateView.as_view(), name='edit_profile'),
    path('create_profile/', ProfileCreateView.as_view(), name='create_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/passwordresetdone.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/passwordresetconfirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/passwordresetcomplete.html'),name='password_reset_complete'),

]

# path('profile/', ProfileView.as_view(), name='profile'),
# path('profile/edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
# path('profile/delete_profile/', ProfileDeleteView.as_view(), name='delete_profile'),
