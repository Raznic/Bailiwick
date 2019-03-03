import uuid
from django.core import validators
from django.db import models
from django.urls import reverse


class Domain(models.Model):

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=255,
        blank=False,
        unique=True,
        validators=[
            validators.RegexValidator(
                # Regex obtained from O'Reilly Regular Expressions Cookbook
                # https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch08s15.html
                regex=r"^((?=[a-z0-9-]{1,63}\.)[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}$",
                message="Not a valid domain name."
            )
        ],
        error_messages={
            "blank": "Domain name cannot be blank.",
            "max_length": "Domain name cannot exceed 255 characters.",
            "unique": "Domain name must be unique."
        }
    )
    registry = models.ForeignKey(
        'registries.Registry',
        on_delete=models.PROTECT,
        related_name="domains"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('domain-detail', args=[str(self.id)])
