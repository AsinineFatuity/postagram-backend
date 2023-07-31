from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate

from core.user.serializers import UserSerializer
from core.user.models import User


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # allow user to login with both email and username
        username_or_email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=username_or_email,
            password=password,
        )
        if user is None:
            try:
                db_user = User.objects.get(username=username_or_email)
                user = authenticate(
                    request=self.context.get("request"),
                    username=db_user.email,
                    password=password,
                )
            except User.DoesNotExist:
                pass
        if user:
            # modify the initial attrs so that we ensure it is the username passed
            attrs["email"] = user.email
            data = super().validate(attrs)
            refresh = self.get_token(self.user)
            data["user"] = UserSerializer(self.user).data
            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            if api_settings.UPDATE_LAST_LOGIN:
                update_last_login(None, self.user)
            return data
