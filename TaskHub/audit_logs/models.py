from django.db import models
from user.models import User

class AuditLog(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    action = models.CharField(max_length=255)

    model_name = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)

    details = models.JSONField()