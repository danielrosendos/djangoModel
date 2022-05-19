import datetime

from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import check_password

from rest_framework import mixins, viewsets, status

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from ...user.Models.UserModel import UserModel

from ...core.Views.CoreViews import CoreView
from ...core.Utils.UtilsCore import get_cache, set_cache

from ..Models.TokenModels import TokenModels
from ..Docs.AuthenticationViewDocs import AuthenticationViewDocs
from ..Serializers.AuthenticationSerializer import AuthenticationSerializer

class AuthenticationView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    class Meta:
        model = TokenModels
        fields = "__all__"

    permission_classes_by_action = {
        'create': [AllowAny]
    }
    serializer_class = AuthenticationSerializer

    @swagger_auto_schema(
        security=AuthenticationViewDocs.createToken.get('security'),
        tags=AuthenticationViewDocs.createToken.get('tags'),
        operation_id=AuthenticationViewDocs.createToken.get('operation_id'),
        operation_summary=AuthenticationViewDocs.createToken.get('operation_summary'),
        operation_description=AuthenticationViewDocs.createToken.get('operation_description'),
        responses=AuthenticationViewDocs.createToken.get('responses')
    )
    def create(self, request, *args, **kwargs):
        try:
            user = UserModel.objects.get(username=request.data.get('username'))
        except Exception as e:
            return Response(
                {
                    "message": "Usuário não encontrado",
                    "data": e.args
                },
                status.HTTP_400_BAD_REQUEST
            )

        if not check_password(request.data.get('password'), user.password):
            return Response(
                {
                    "message": "Não foi possível autenticar o usuário",
                    "data": []
                },
                status.HTTP_401_UNAUTHORIZED
            )

        token_cache = get_cache(name='token_cache_' + str(user.id))

        if token_cache:
            return Response(
                {
                    "message": "Usuário logado com sucesso",
                    "data": {
                        'refresh': str(token_cache.get('refresh_token')),
                        'access': str(token_cache.get('access_token')),
                        'msg': 'Veio da cache'
                    }
                },
                status.HTTP_200_OK
            )

        token = TokenModels.objects.filter(
            user_id=user.id,
            life_time__gte=datetime.datetime.now()
        )

        if token:
            set_cache(
                name='token_cache_' + str(user.id),
                payload={
                    'access_token': str(token.get().access_token),
                    'refresh_token': str(token.get().refresh_token),
                    'time': token.get().life_time
                }
            )

            return Response(
                {
                    "message": "Usuário logado com sucesso",
                    "data": {
                        'refresh': str(token.get().refresh_token),
                        'access': str(token.get().access_token),
                        'msg': 'Veio do banco'
                    }
                },
                status.HTTP_200_OK
            )

        token = RefreshToken.for_user(user)

        TokenModels.objects.filter(
            user_id=user.id
        ).order_by('id').first().delete()

        TokenModels.objects.update_or_create(
            user_id=user.id,
            access_token=token.access_token,
            refresh_token=token,
            life_time=datetime.datetime.now() + token.lifetime
        )

        set_cache(
            name='token_cache_' + str(user.id),
            payload={
                'access_token': token.access_token,
                'refresh_token': token,
                'time': datetime.datetime.now() + token.lifetime
            }
        )

        return Response(
            {
                "message": "Usuário logado com sucesso",
                "data": {
                    'refresh': str(token),
                    'access': str(token.access_token),
                    'msg': 'Token Novo'
                }
            },
            status.HTTP_200_OK
        )

    def get_permissions(self):
        return CoreView.get_permissions(self)