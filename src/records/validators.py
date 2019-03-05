import re
from django.core.exceptions import ValidationError


def validate_owner_subdomain(owner: str, domain: str) -> None:
    """
    Validate that an owner is equal to, or a sub-domain of, a domain.
    :param owner:
    :param domain:
    :return:
    """
    subdomain_regex = f"^([a-z0-9]+(-[a-z0-9]+)*\\.)*{domain}$"
    if owner and not re.match(re.compile(subdomain_regex), str(owner)):
        raise ValidationError({
            "owner": "Owner must either be the current domain or a sub-domain."
        })
