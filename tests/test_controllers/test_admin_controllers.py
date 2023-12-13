from unittest import TestCase, mock
from src.controllers.admin_controllers import AdminControllers


class TestAssetDataController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.admin_contoller_obj = AdminControllers()

    @mock.patch("src.controllers.admin_controllers.db")
    def test_create_new_user(self, mock_db) -> None:
        mock_db.save_data.return_value = None
        function_call = self.admin_contoller_obj.create_new_user("role", "name", "pwd")
        self.assertEqual(function_call, None)
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.admin_controllers.db")
    def test_deactivate_vendor_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = ["data"]
        mock_db.save_data.return_value = None
        self.assertTrue(self.admin_contoller_obj.deactivate_vendor("kris@gmail.com"))
        mock_db.fetch_data.assert_called_once()
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.admin_controllers.db")
    def test_deactivate_vendor_negative(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.admin_contoller_obj.deactivate_vendor("kris@gmail.com"))
        mock_db.fetch_data.assert_called_once()
