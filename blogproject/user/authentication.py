from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from post.models import BlacklistedAccessToken

class CustomJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        if BlacklistedAccessToken.objects.filter(token=raw_token).exists():
            raise AuthenticationFailed("This token has been blacklisted.")
        return super().get_validated_token(raw_token)