from django.core.validators import ValidationError
from django.test import TestCase
from domains.factory import DomainFactory
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
                "Cannot be blank."
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
                "Cannot exceed 63 characters."
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


class NsRecordTestCase(TestCase):
    """
    Test case for NS records.
    """

    def test_long_name_server(self):
        """
        Ensure name_server cannot exceed 255 characters.
        """
        expected_errors = {
            "name_server": [
                "Cannot exceed 255 characters."
            ]
        }
        name = "test." * 51 + "local"
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.NsRecordFactory.create(name_server=name).full_clean()

    def test_long_owner(self):
        """
        Ensure owner cannot exceed 255 characters.
        """
        expected_errors = {
            "owner": [
                "Cannot exceed 255 characters."
            ]
        }
        name = "test." * 51 + "local"
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.NsRecordFactory.create(
                domain=DomainFactory.create(name="local"),
                owner=name
            ).full_clean()

    def test_owner_subdomain(self):
        """
        Verify that the owner must always be either the current domain or a sub-domain.
        """
        expected_errors = {
            "owner": [
                "Owner must either be the current domain or a sub-domain."
            ]
        }
        domain = DomainFactory.create(name="example.com")
        # Good
        factory.NsRecordFactory.create(domain=domain, owner="").full_clean()
        factory.NsRecordFactory.create(domain=domain, owner="example.com").full_clean()
        factory.NsRecordFactory.create(domain=domain, owner="test.example.com").full_clean()
        factory.NsRecordFactory.create(domain=domain, owner="sub.test.example.com").full_clean()
        # Bad
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.NsRecordFactory.create(domain=domain, owner="example.org").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.NsRecordFactory.create(domain=domain, owner="aexample.com").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.NsRecordFactory.create(domain=domain, owner="example.com.org").full_clean()


class MxRecordTestCase(TestCase):
    """
    Test case for MX records.
    """

    def test_long_mail_exhange(self):
        """
        Ensure mail_exchange cannot exceed 255 characters.
        """
        expected_errors = {
            "mail_exchange": [
                "Cannot exceed 255 characters."
            ]
        }
        name = "test." * 51 + "local"
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.MxRecordFactory.create(mail_exchange=name).full_clean()

    def test_long_owner(self):
        """
        Ensure owner cannot exceed 255 characters.
        """
        expected_errors = {
            "owner": [
                "Cannot exceed 255 characters."
            ]
        }
        name = "test." * 51 + "local"
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.MxRecordFactory.create(
                domain=DomainFactory.create(name="local"),
                owner=name
            ).full_clean()

    def test_owner_subdomain(self):
        """
        Verify that the owner must always be either the current domain or a sub-domain.
        """
        expected_errors = {
            "owner": [
                "Owner must either be the current domain or a sub-domain."
            ]
        }
        domain = DomainFactory.create(name="example.com")
        # Good
        factory.MxRecordFactory.create(domain=domain, owner="").full_clean()
        factory.MxRecordFactory.create(domain=domain, owner="example.com").full_clean()
        factory.MxRecordFactory.create(domain=domain, owner="test.example.com").full_clean()
        factory.MxRecordFactory.create(domain=domain, owner="sub.test.example.com").full_clean()
        # Bad
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.MxRecordFactory.create(domain=domain, owner="example.org").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.MxRecordFactory.create(domain=domain, owner="aexample.com").full_clean()
        with self.assertRaisesMessage(ValidationError, str(expected_errors)):
            factory.MxRecordFactory.create(domain=domain, owner="example.com.org").full_clean()
