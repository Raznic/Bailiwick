import uuid
from django.db import models
from django.urls import reverse


class Registry(models.Model):

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=120,
        blank=False,
        unique=True,
        error_messages={
            "blank": "Registry name cannot be blank.",
            "max_length": "Registry name cannot exceed 120 characters.",
            "unique": "Registry name must be unique."
        }
    )

    def get_absolute_url(self):
        return reverse('registry-detail', args=[str(self.id)])
