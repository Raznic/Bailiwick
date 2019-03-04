from django.core.validators import ValidationError
from django.test import TestCase
from .. import factory


class ARecordTestCase(TestCase):
    """
    Test case for A records.
    """
    def test_blank_hostname(self):
        """
        Ensure hostname field cannot be blank.
        """
        expected_errors = {
            "hostname": [
                "Hostname cannot be blank."
            ]
        }
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.ARecordFactory.create(hostname="").full_clean()

    def test_long_hostname(self):
        """
        Ensure hostname cannot exceed 63 characters.
        """
        expected_errors = {
            "hostname": [
                "Hostname cannot exceed 63 characters."
            ]
        }
        name = "a" * 64
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.ARecordFactory.create(hostname=name).full_clean()

    def test_hostname_special_characters(self):
        """
        Ensure hostnames cannot contain special characters.
        """
        expected_errors = {
            "hostname": [
                "Not a valid hostname."
            ]
        }
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.ARecordFactory.create(hostname="www?").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.ARecordFactory.create(hostname="www$").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.ARecordFactory.create(hostname="www!").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.ARecordFactory.create(hostname="www.").full_clean()
