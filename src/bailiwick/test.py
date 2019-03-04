class ListViewTestSuite:
    """
    Tests for ListView.
    """
    root_url = None

    def test_list_view(self):
        """
        Ensure view returns 200.
        """
        response = self.client.get(f"/{self.root_url}/")
        self.assertEqual(200, response.status_code)


class CreateViewTestSuite:
    """
    Tests for CreateView.
    """
    root_url = None

    def test_create_view(self):
        """
        Ensure view returns 200.
        """
        response = self.client.get(f"/{self.root_url}/new/")
        self.assertEqual(200, response.status_code)


class DetailViewTestSuite:
    """
    Tests for DetailView.
    """
    root_url = None
    model_factory = None

    def test_detail_view(self):
        """
        Ensure view returns 200.
        """
        obj = self.model_factory.create()
        response = self.client.get(f"/{self.root_url}/{str(obj.id)}/")
        self.assertEqual(200, response.status_code)


class UpdateViewTestSuite:
    """
    Tests for UpdateView.
    """
    root_url = None
    model_factory = None

    def test_update_view(self):
        """
        Ensure view returns 200.
        """
        obj = self.model_factory.create()
        response = self.client.get(f"/{self.root_url}/{str(obj.id)}/edit/")
        self.assertEqual(200, response.status_code)


class DeleteViewTestSuite:
    """
    Tests for DeleteView.
    """
    root_url = None
    model_factory = None

    def test_delete_view(self):
        """
        Ensure view returns 200.
        """
        obj = self.model_factory.create()
        response = self.client.get(f"/{self.root_url}/{str(obj.id)}/delete/")
        self.assertEqual(200, response.status_code)


class ModelViewTestSuite(
    ListViewTestSuite,
    CreateViewTestSuite,
    DetailViewTestSuite,
    UpdateViewTestSuite,
    DeleteViewTestSuite
):
    pass
