from drf_yasg import openapi
from rest_framework import status
from ...core.Serializers.CoreResponseSerializer import ResponseSerializer

class UserViewDocs:
    createUser = {
        "security": [{
            "SECURITY_DEFINITIONS": {
                'Basic': {
                    'type': None
                }
            },
            "USE_SESSION_AUTH": False
        }],
        "tags": ["Usuário"],
        "operation_id":'create_user',
        "operation_summary": 'Criação de usuário',
        "operation_description":'Rota para criação de usuário',
        "responses": {
            status.HTTP_201_CREATED: openapi.Response(
                description='Usuário Criado com Sucesso',
                examples={
                    "application/json": {
                        "message": "Usuário criado com sucesso",
                        "data": []
                    }
                },
                schema=ResponseSerializer
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description='Usuário não cadastrado',
                examples={
                    "application/json": {
                        "message": "Error ao criar o usuário",
                        "data": {
                            "errors": {
                                "username": [
                                    "Usuário com este username já existe."
                                ],
                                "email": [
                                    "Usuário com este email já existe."
                                ]
                            }
                        }
                    }
                },
                schema=ResponseSerializer
            )
        }
    }

    updateUser = {
        'manual_parameters':openapi.Parameter(
            name='Authorization',
            in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            required=True
        ),
        "tags": ["Usuário"],
        "operation_id": 'update_user',
        "operation_summary": 'Atualizar Usuário',
        "operation_description": 'Rota para atualização do usuário',
        "responses": {
            status.HTTP_201_CREATED: openapi.Response(
                description='Usuário Atualizado com Sucesso',
                examples={
                    "application/json": {
                        "message": "Usuário Atualizado com sucesso",
                        "data": []
                    }
                },
                schema=ResponseSerializer
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description='Não foi possível atualizar as informações do usuário',
                examples={
                    "application/json": {
                        "message": "Error ao criar o usuário",
                        "data": {
                            "errors": {
                                "username": [
                                    "Usuário com este username já existe."
                                ],
                                "email": [
                                    "Usuário com este email já existe."
                                ]
                            }
                        }
                    }
                },
                schema=ResponseSerializer
            )
        }
    }