from django.urls import path
from .Views.UserView import UserView

urlpatterns = [
    path(
        'user/register/',
        UserView.as_view({'post': 'create', 'patch': 'update'}),
        name='register'
    )
]