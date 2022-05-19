from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth.hashers import make_password

from rest_framework.response import Response
from rest_framework import status, mixins, viewsets
from rest_framework.permissions import AllowAny

from ..Models.UserModel import UserModel
from ..Docs.UserViewDocs import UserViewDocs
from ..Serializers.UserSerializer import UserSerializer, UpdateUserSerializar

from ...core.Views.CoreViews import CoreView

from ...authentication.Middleware.AuthorizationPermission import AuthorizationPermission

class UserView(mixins.UpdateModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet, CoreView):
    serializer_class = UserSerializer
    permission_classes_by_action = {
        'create': [AllowAny],
        'update': [AuthorizationPermission]
    }

    def get_serializer_class(self):
        if self.action == 'update':
            return UpdateUserSerializar

        return UserSerializer

    @swagger_auto_schema(
        manual_parameters=[UserViewDocs.updateUser.get('manual_parameters')],
        tags=UserViewDocs.updateUser.get('tags'),
        operation_id=UserViewDocs.updateUser.get('operation_id'),
        operation_summary=UserViewDocs.updateUser.get('operation_summary'),
        operation_description=UserViewDocs.updateUser.get('operation_description'),
        responses=UserViewDocs.updateUser.get('responses')
    )
    def update(self, request, *args, **kwargs):
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

        if UserModel.objects.filter(email=request.data.get('email')):
            return Response(
                {
                    "message": "E-mail já cadastrado",
                    "data": []
                },
                status.HTTP_400_BAD_REQUEST
            )

        if request.data.get('new_username'):
            if UserModel.objects.filter(username=request.data.get('new_username', '""')):
                return Response(
                    {
                        "message": "Usuário já cadastrado",
                        "data": []
                    },
                    status.HTTP_400_BAD_REQUEST
                )

        UserModel.objects.filter(id=user.id).update(
                email=request.data.get('email'),
                username= request.data.get('username')
            )

        return Response(
            {
                "message": "Usuário atualizado com sucesso",
                "data": []
            },
            status.HTTP_200_OK
        )


    @swagger_auto_schema(
        security=UserViewDocs.createUser.get('security'),
        tags=UserViewDocs.createUser.get('tags'),
        operation_id=UserViewDocs.createUser.get('operation_id'),
        operation_summary=UserViewDocs.createUser.get('operation_summary'),
        operation_description=UserViewDocs.createUser.get('operation_description'),
        responses=UserViewDocs.createUser.get('responses')
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response(
                {
                    "message": "Error ao criar o usuário",
                    "data": {
                        "errors": serializer.errors
                    }
                },
                status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        data['password'] = make_password(data['password'])
        request.data.update(data)
        super(UserView, self).create(request, *args, **kwargs)

        return Response(
            {
                "message": "Usuário criado com sucesso",
                "data": []
            },
            status.HTTP_201_CREATED
        )

    def get_permissions(self):
        return CoreView.get_permissions(self)