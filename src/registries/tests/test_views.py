from django.test import TestCase
from bailiwick.test import ModelViewTestSuite
from .. import factory


class RegistryViewTestCase(ModelViewTestSuite, TestCase):
    root_url = "registries"
    model_factory = factory.RegistryFactory
