from django.test import TestCase
from bailiwick.test import ModelViewTestSuite
from .. import factory


class DomainViewTestCase(ModelViewTestSuite, TestCase):
    root_url = "domains"
    model_factory = factory.DomainFactory

