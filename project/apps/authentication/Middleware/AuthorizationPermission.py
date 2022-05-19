import datetime

from rest_framework import permissions

from ..Models.TokenModels import TokenModels

from ...user.Models.UserModel import UserModel
from ...core.Utils.UtilsCore import get_cache, set_cache, decode_token

class AuthorizationPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.META.get('HTTP_AUTHORIZATION', '')[len('Bearer '):]

        if not token:
            return False

        token_decoded = decode_token(token)
        user_id = str(token_decoded.get('user_id'))
        name_cache = 'token_cache_' + user_id

        token_cached = get_cache(name=name_cache)

        if token_cached and datetime.datetime.now().isoformat() < token_cached.get('time').isoformat():
            return True


        token_valid = TokenModels.objects.filter(
            user_id=token_decoded.get('user_id'),
            access_token=token,
            life_time__gte=datetime.datetime.now()
        )

        user_valid = UserModel.objects.filter(
            id=token_decoded.get('user_id')
        )

        if token_valid and user_valid:
            set_cache(
                name=name_cache,
                payload={
                    'access_token': str(token_valid.get().access_token),
                    'refresh_token': str(token_valid.get().refresh_token),
                    'time': token_valid.get().life_time
                }
            )
            return True

        return False