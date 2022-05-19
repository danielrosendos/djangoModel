from drf_yasg import openapi
from rest_framework import status
from ...core.Serializers.CoreResponseSerializer import ResponseSerializer

class AuthenticationViewDocs:
    createToken = {
        "security": [{
            "SECURITY_DEFINITIONS": {
                'Basic': {
                    'type': None
                }
            },
            "USE_SESSION_AUTH": False
        }],
        "tags": ["Login"],
        "operation_id": "login_user",
        "operation_summary": "Criar autenticação do usuário",
        "operation_description": "Rota para autenticação do usuário",
        "responses": {
            status.HTTP_200_OK: openapi.Response(
                description='Usuário logado com sucesso',
                examples={
                    "application/json": {
                        "message": "Usuário logado com sucesso",
                        "data": {
                            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mjk2ODAwNiwiaWF0IjoxNjUyODgxNjA2LCJqdGkiOiJkNzY0MGY0OTZiYjk0ZjE0OGViMWFkMDM0ZWU2ZTRiNCIsInVzZXJfaWQiOjExfQ.l2quSJg6NxtP9-rZLIiwGSivL8FLnsLcD9ie_pPwCe4",
                            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mjk2ODAwNiwiaWF0IjoxNjUyODgxNjA2LCJqdGkiOiJkNzY0MGY0OTZiYjk0ZjE0OGViMWFkMDM0ZWU2ZTRiNCIsInVzZXJfaWQiOjExfQ.l2quSJg6NxtP9-rZLIiwGSivL8FLnsLcD9ie_pPwCe4",
                        }
                    }
                },
                schema=ResponseSerializer
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Usuário não encontrado",
                examples={
                    "application/json": {
                        "message": "Usuário não encontrado",
                        "data": []
                    }
                },
                schema=ResponseSerializer
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description="Não foi possível autenticar o usuário",
                examples={
                    "application/json": {
                        "message": "Não foi possível autenticar o usuário",
                        "data": []
                    }
                },
                schema=ResponseSerializer
            )
        }
    }