from django.db import models


class Conversation(models.Model):
    CONVERSATION_TYPES = (
        (1, "pv"),
        (2, "group"),
        (3, "channel"),
        (4, "bot")
    )
    type = models.IntegerField(choices=CONVERSATION_TYPES)

