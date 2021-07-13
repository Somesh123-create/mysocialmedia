from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('Log_in/', LogInView.as_view(), name='Log_in'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
]
