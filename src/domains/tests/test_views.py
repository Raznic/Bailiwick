from django.test import TestCase
from .. import factory


class DomainListViewTestCase(TestCase):
    """
    Test case for DomainListView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        response = self.client.get("/domains/")
        self.assertEqual(200, response.status_code)


class DomainDetailViewTestCase(TestCase):
    """
    Test case for DomainDetailView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        obj = factory.DomainFactory.create()
        response = self.client.get(f"/domains/{str(obj.id)}/")
        self.assertEqual(200, response.status_code)


class DomainCreateViewTestCase(TestCase):
    """
    Test case for DomainCreateView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        response = self.client.get("/domains/new/")
        self.assertEqual(200, response.status_code)


class DomainUpdateViewTestCase(TestCase):
    """
    Test case for DomainUpdateView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        obj = factory.DomainFactory.create()
        response = self.client.get(f"/domains/{str(obj.id)}/edit/")
        self.assertEqual(200, response.status_code)


class DomainDeleteViewTestCase(TestCase):
    """
    Test case for DomainDeleteView.
    """

    def test_view(self):
        """
        Ensure view returns 200.
        """
        obj = factory.DomainFactory.create()
        response = self.client.get(f"/domains/{str(obj.id)}/delete/")
        self.assertEqual(200, response.status_code)
