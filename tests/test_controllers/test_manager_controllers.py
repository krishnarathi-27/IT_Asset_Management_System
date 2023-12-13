from unittest import mock, TestCase
from src.controllers.manager_controllers import ManagerControllers


class TestManagerControllers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj_manager = ManagerControllers()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_fetch_by_category(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_manager.fetch_by_category("CATsdwe"), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_fetch_by_vendor(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_manager.fetch_by_vendor("VENsdwe"), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_fetch_asset_available(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_manager.fetch_asset_available(), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_fetch_asset_maintenance(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_manager.fetch_asset_maintenance(), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_view_pending_issues(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_manager.view_pending_issues(), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_send_asset_positive(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        mock_db.save_data.return_value = None
        self.assertTrue(self.obj_manager.send_asset("ISNdsade", "EMP98cs"))
        mock_db.fetch_data.assert_called_once()
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_send_asset_negative(self, mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.obj_manager.send_asset("ISNdsade", "EMP98cs"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_receive_asset_positive(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        mock_db.save_data.return_value = None
        self.assertTrue(self.obj_manager.recieve_asset("ISNdsade"))
        mock_db.fetch_data.assert_called_once()
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_recieve_asset_negative(self, mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.obj_manager.recieve_asset("ISNdsade"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_display_maintenance_table(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_manager.display_maintenance_table(), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.manager_controllers.db")
    def test_fetch_by_username_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_manager.fetch_by_username("EMPsdf4"), ["data"])
        self.assertEqual(mock_db.fetch_data.call_count, 2)

    @mock.patch("src.controllers.manager_controllers.db")
    def test_fetch_by_username_negative(self, mock_db) -> None:
        mock_db.fetch_data.side_effect = [[], ["data"], []]
        self.assertFalse(self.obj_manager.fetch_by_username("EMPsdf4"))
        self.assertFalse(self.obj_manager.fetch_by_username("EMPsdf4"))
        self.assertEqual(mock_db.fetch_data.call_count, 3)
