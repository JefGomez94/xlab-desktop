from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('get_login/', views.get_login, name='get_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_User/', views.get_User, name='get_User'),
]