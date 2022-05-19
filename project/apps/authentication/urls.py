from django.urls import path
from .Views.AuthenticationView import AuthenticationView

urlpatterns = [
    path(
        'user/login/',
        AuthenticationView.as_view({'post': 'create'}),
        name='login'
    )
]