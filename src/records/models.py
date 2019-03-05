import re
import uuid
from django.core import validators, exceptions
from django.db import models
from django.urls import reverse
from bailiwick import regex


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
                regex=regex.HOSTNAME_REGEX,
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

    def get_absolute_url(self):
        return reverse('a-record-detail', args=[str(self.id)])


class NsRecord(models.Model):

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    name_server = models.CharField(
        max_length=255,
        blank=False,
        validators=[
            validators.RegexValidator(
                regex=regex.FQDN_REGEX,
                message="Name server must by a fully-qualified domain name."
            ),
        ],
        error_messages={
            "blank": "Name server cannot be blank.",
            "max_length": "Name server cannot exceed 255 characters.",
        }
    )
    owner = models.CharField(
        max_length=255,
        default="",
        blank=True,
        validators=[
            validators.RegexValidator(
                regex=regex.FQDN_REGEX,
                message="Owner must be a fully-qualified domain name."
            ),
        ],
        error_messages={
            "max_length": "Owner cannot exceed 255 characters.",
        },
        help_text="The domain the name server is authoritative for. Can be the current domain or a sub-domain. " +
                  "If not defined, assume the name server is authoritative for the current domain."
    )
    domain = models.ForeignKey(
        "domains.Domain",
        on_delete=models.CASCADE,
        related_name="ns_records",
    )
    time_to_live = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=None,
        help_text="Time in seconds for how long record should be cached by a resolver. " +
                  "If not set, inherited from domain."
    )

    def __str__(self):
        return self.name_server

    def get_absolute_url(self):
        return reverse('ns-record-detail', args=[str(self.id)])

    def clean(self):
        # Ensure owner is a sub-domain of associated domain object
        subdomain_regex = f"^([a-z0-9]+(-[a-z0-9]+)*\\.)*{self.domain.name}$"
        if self.owner and not re.match(re.compile(subdomain_regex), str(self.owner)):
            raise exceptions.ValidationError({
                "owner": "Owner must either be the current domain or a sub-domain."
            })
