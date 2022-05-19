from djongo import models

from ...core.Models.CoreModel import CoreModel

class UserModel(CoreModel):
    username = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        error_messages={'unique': "Usuário Já cadastrado"},
        null=False
    )

    password = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
        error_messages={'invalid': "Digite um endereço de e-mail válido"}
    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']