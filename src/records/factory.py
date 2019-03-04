import factory
from . import models


class ARecordFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.ARecord

    hostname = factory.Sequence(lambda n: f"host-{n}")
    address = factory.Faker('ipv4')
    domain = factory.SubFactory('domains.factory.DomainFactory')
