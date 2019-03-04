from django.core.validators import ValidationError
from django.test import TestCase
from .. import factory


class DomainTestCase(TestCase):
    """
    Test case for Domain model.
    """

    def test_blank_name(self):
        """
        Ensure name field cannot be blank.
        """
        expected_errors = {
            "name": [
                "Domain name cannot be blank."
            ]
        }
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.create(name="").full_clean()

    def test_long_name(self):
        """
        Ensure name cannot exceed 255 characters.
        """
        expected_errors = {
            "name": [
                "Domain name cannot exceed 255 characters."
            ]
        }
        name = "test." * 51 + "com"
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.create(name=name).full_clean()

    def test_unique_name(self):
        """
        Ensure name must be unique.
        """
        expected_errors = {
            "name": [
                "Domain name must be unique."
            ]
        }
        name = "example.com"
        factory.DomainFactory.create(name=name)
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.build(name=name).validate_unique()

    def test_name_label_starts_with_hyphen(self):
        """
        Ensure name label cannot start with hyphen.
        """
        expected_errors = {
            "name": [
                "Not a valid domain name."
            ]
        }
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.create(name="-example.com").full_clean()

    def test_name_label_ends_with_hyphen(self):
        """
        Ensure name label cannot end with hyphen.
        """
        expected_errors = {
            "name": [
                "Not a valid domain name."
            ]
        }
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.create(name="example-.com").full_clean()

    def test_name_special_characters(self):
        """
        Ensure names cannot contain special characters.
        """
        expected_errors = {
            "name": [
                "Not a valid domain name."
            ]
        }
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.create(name="example?.com").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.create(name="example$.com").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.create(name="example!.com").full_clean()

    def test_name_trailing_period(self):
        """
        Ensure names cannot end with a period.
        """
        expected_errors = {
            "name": [
                "Not a valid domain name."
            ]
        }
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.create(name="example.com.").full_clean()

    def test_name_with_capitals(self):
        """
        Ensure name with capitals is valid.
        """
        factory.DomainFactory.create(name="EXAMPLE.COM")

    def test_name_unique_case_insensitivity(self):
        """
        Ensure that name uniqueness is not case-sensitive.
        """
        expected_errors = {
            "name": [
                "Domain name must be unique."
            ]
        }
        name = "example.com"
        factory.DomainFactory.create(name=name)
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.DomainFactory.build(name=name.upper()).validate_unique()
