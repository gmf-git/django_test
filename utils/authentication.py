from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions as e

from system.models import UserModel


class DefineAuth:
    def authenticate(self, request, username, password):
        try:
            user = UserModel.objects.get(username=username, password=password)
            return user
        except Exception:
            return


class IsAuthentication:
    def authenticate(self, request):
        auth = get_authorization_header(request)
        path = request._request.path
        if 'docs' in path:
            return None
        if not auth:
            raise e.AuthenticationFailed('请携带认证信息')
