from djongo import models
from ...core.Models.CoreModel import CoreModel

class TokenModels(CoreModel):
    user_id = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )

    access_token = models.TextField(
        null=False,
        blank=False
    )

    refresh_token = models.TextField(
        null=False,
        blank=False
    )

    life_time = models.DateTimeField()