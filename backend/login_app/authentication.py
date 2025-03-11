from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from orders.models import Appusers

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, usr_identification=None, password=None):
        try:
            user = Appusers.objects.get(usr_identification=usr_identification)
            if check_password(password, user.usr_password):
                return user
        except Appusers.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Appusers.objects.get(pk=user_id)
        except Appusers.DoesNotExist:
            return None

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
            return Appusers.objects.get(id=user_id)
        except Appusers.DoesNotExist:
            return None

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)
        return (user, validated_token) if user else None