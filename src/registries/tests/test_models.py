from django.core.validators import ValidationError
from django.test import TestCase
from .. import factory


class RegistryTestCase(TestCase):
    """
    Test case for Registry model.
    """

    def test_blank_name(self):
        """
        Ensure Registry cannot have a blank name.
        """
        expected_errors = {
            "name": [
                "Registry name cannot be blank."
            ]
        }
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.RegistryFactory.build(name="").full_clean()

    def test_long_name(self):
        """
        Ensure Registry cannot have a name longer than 120 characters.
        """
        expected_errors = {
            "name": [
                "Registry name cannot exceed 120 characters."
            ]
        }
        name = "Registry " + "A" * 120
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.RegistryFactory.build(name=name).full_clean()

    def test_unique_name(self):
        """
        Ensure that Registry is unique.
        """
        expected_errors = {
            "name": [
                "Registry name must be unique."
            ]
        }
        name = "My Registry"
        factory.RegistryFactory.create(name=name)
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.RegistryFactory.build(name=name).full_clean()
