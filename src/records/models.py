import uuid
from django.core.validators import RegexValidator, validate_ipv4_address
from django.db import models
from django.urls import reverse
from bailiwick import regex
from . import validators


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
            RegexValidator(
                regex=regex.HOSTNAME_REGEX,
                message="Not a valid hostname."
            ),
        ],
        error_messages={
            "blank": "Cannot be blank.",
            "max_length": "Cannot exceed 63 characters.",
        }
    )
    address = models.GenericIPAddressField(
        protocol="IPv4",
        blank=False,
        validators=[
           validate_ipv4_address,
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
            RegexValidator(
                regex=regex.FQDN_REGEX,
                message="Name server must by a fully-qualified domain name."
            ),
        ],
        error_messages={
            "blank": "Cannot be blank.",
            "max_length": "Cannot exceed 255 characters.",
        }
    )
    owner = models.CharField(
        max_length=255,
        default="",
        blank=True,
        validators=[
            RegexValidator(
                regex=regex.FQDN_REGEX,
                message="Owner must be a fully-qualified domain name."
            ),
        ],
        error_messages={
            "max_length": "Cannot exceed 255 characters.",
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
        validators.validate_owner_subdomain(str(self.owner), self.domain.name)


class MxRecord(models.Model):

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    mail_exchange = models.CharField(
        max_length=255,
        blank=False,
        validators=[
            RegexValidator(
                regex=regex.FQDN_REGEX,
                message="Must be a fully-qualified domain name."
            ),
        ],
        error_messages={
            "blank": "Cannot be blank.",
            "max_length": "Cannot exceed 255 characters.",
        }
    )
    owner = models.CharField(
        max_length=255,
        default="",
        blank=True,
        validators=[
            RegexValidator(
                regex=regex.FQDN_REGEX,
                message="Owner must be a fully-qualified domain name."
            ),
        ],
        error_messages={
            "max_length": "Cannot exceed 255 characters.",
        },
        help_text="The domain the mail exchange is authoritative for. Can be the current domain or a sub-domain. " +
                  "If not defined, assume the mail exchange is authoritative for the current domain."
    )
    preference = models.PositiveIntegerField(
        default=10,
        help_text="Preference for using this mail exchange server over others. " +
                  "Lower values indicate a higher preference."
    )
    domain = models.ForeignKey(
        "domains.Domain",
        on_delete=models.CASCADE,
        related_name="mx_records",
    )
    time_to_live = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=None,
        help_text="Time in seconds for how long record should be cached by a resolver. " +
                  "If not set, inherited from domain."
    )

    def __str__(self):
        return self.mail_exchange

    def get_absolute_url(self):
        return reverse('mx-record-detail', args=[str(self.id)])

    def clean(self):
        validators.validate_owner_subdomain(str(self.owner), self.domain.name)
