from django.db import models
from tasks.models import Task

class GeneratedImage(models.Model):

    IMAGE_TYPES = (
        ("white_bg", "White Background"),
        ("theme", "Theme"),
        ("creative", "Creative"),
        ("model_front", "Model Front"),
        ("model_side", "Model Side"),
        ("model_closeup", "Model Closeup"),
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="generated_images"
    )

    image = models.ImageField(
        upload_to="generated/"
    )

    image_type = models.CharField(
        max_length=100,
        choices=IMAGE_TYPES
    )

    prompt_used = models.TextField()

    metadata = models.JSONField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )