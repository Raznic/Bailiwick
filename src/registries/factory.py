import factory
from . import models


class RegistryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Registry

    name = factory.Sequence(lambda n: f"Registry {n}")
