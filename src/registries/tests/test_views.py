from django.test import TestCase
from .. import factory


class RegistryListViewTestCase(TestCase):
    """
    Test case for RegistryListView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        response = self.client.get("/registries/")
        self.assertEqual(200, response.status_code)


class RegistryDetailViewTestCase(TestCase):
    """
    Test case for RegistryDetailView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        obj = factory.RegistryFactory.create()
        response = self.client.get(f"/registries/{str(obj.id)}/")
        self.assertEqual(200, response.status_code)


class RegistryCreateViewTestCase(TestCase):
    """
    Test case for RegistryCreateView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        response = self.client.get("/registries/new/")
        self.assertEqual(200, response.status_code)


class RegistryUpdateViewTestCase(TestCase):
    """
    Test case for RegistryUpdateView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        obj = factory.RegistryFactory.create()
        response = self.client.get(f"/registries/{str(obj.id)}/edit/")
        self.assertEqual(200, response.status_code)


class RegistryDeleteViewTestCase(TestCase):
    """
    Test case for RegistryDeleteView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        obj = factory.RegistryFactory.create()
        response = self.client.get(f"/registries/{str(obj.id)}/delete/")
        self.assertEqual(200, response.status_code)
