import uuid
from django.core import validators
from django.db import models


class ARecord(models.Model):

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    hostname = models.CharField(
        max_length=63,
        blank=False,
        validators=[
            validators.RegexValidator(
                regex=r"^[a-z0-9]+(-[a-z0-9]+)*$",
                message="Not a valid hostname."
            ),
        ],
        error_messages={
            "blank": "Hostname cannot be blank.",
            "max_length": "Hostname cannot exceed 63 characters.",
        }
    )
    address = models.GenericIPAddressField(
        protocol="IPv4",
        blank=False,
        validators=[
            validators.validate_ipv4_address,
        ]
    )
    domain = models.ForeignKey(
        "domains.Domain",
        on_delete=models.CASCADE,
        related_name="a_records",
    )
    time_to_live = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=None,
        help_text="Time in seconds for how long record should be cached by a resolver. " +
                  "If not set, inherited from domain."
    )

    def __str__(self):
        return self.hostname
