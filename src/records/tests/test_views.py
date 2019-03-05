from django.test import TestCase
from bailiwick.test import ModelViewTestSuite
from .. import factory


class ARecordViewTestCase(ModelViewTestSuite, TestCase):
    root_url = "records/a"
    model_factory = factory.ARecordFactory


class NsRecordViewTestCase(ModelViewTestSuite, TestCase):
    root_url = "records/ns"
    model_factory = factory.NsRecordFactory
