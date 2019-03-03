import factory
from . import models


class DomainFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Domain

    name = factory.Sequence(lambda n: f"example{n}.com")
    registry = factory.SubFactory('registries.factory.RegistryFactory')
