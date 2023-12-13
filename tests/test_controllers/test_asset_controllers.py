from unittest import mock, TestCase
from src.controllers.asset_controllers import AssetControllers


class TestAssetControllers(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj_asset_controller = AssetControllers()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_view_asset_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_asset_controller.view_asset(), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_view_asset_negative(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        self.assertEqual(self.obj_asset_controller.view_asset(), [])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_display_mapping_id_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.obj_asset_controller.display_mapping_id(), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_display_mapping_id_negative(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        self.assertEqual(self.obj_asset_controller.display_mapping_id(), [])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_add_asset_to_inventory_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = ["data"]
        mock_db.save_data.return_value = None
        self.assertTrue(
            self.obj_asset_controller.add_asset_to_inventory("as", "as", "as")
        )
        mock_db.fetch_data.asset_called_once()
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_add_asset_to_inventory_negative(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        self.assertFalse(
            self.obj_asset_controller.add_asset_to_inventory("as", "as", "as")
        )
        mock_db.fetch_data.asset_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_view_assignable_asset_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = ["data"]
        self.assertTrue(self.obj_asset_controller.view_assignable_asset())
        mock_db.fetch_data.asset_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_view_assignable_asset_negative(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.obj_asset_controller.view_assignable_asset())
        mock_db.fetch_data.asset_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_assign_asset_negative(self, mock_db) -> None:
        mock_db.fetch_data.side_effect = [[], ["data"], []]
        self.assertFalse(self.obj_asset_controller.assign_asset("as", "sa"))
        self.assertFalse(self.obj_asset_controller.assign_asset("as", "sa"))
        self.assertEqual(mock_db.fetch_data.call_count, 3)

    @mock.patch("src.controllers.asset_controllers.db")
    def test_assign_asset_positive(self, mock_db) -> None:
        mock_db.fetch_data.side_effect = [["data"], ["data"]]
        mock_db.save_data.return_value = None
        self.assertTrue(self.obj_asset_controller.assign_asset("as", "sa"))
        self.assertEqual(mock_db.fetch_data.call_count, 2)
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_view_unassignable_asset_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = ["data"]
        self.assertTrue(self.obj_asset_controller.view_unassignable_asset())
        mock_db.fetch_data.asset_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_view_unassignable_asset_negative(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.obj_asset_controller.view_unassignable_asset())
        mock_db.fetch_data.asset_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_unassign_asset_negative(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.obj_asset_controller.unassign_asset("as"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_controllers.db")
    def test_unassign_asset_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = ["data"]
        mock_db.save_data.return_value = None
        self.assertTrue(self.obj_asset_controller.unassign_asset("as"))
        mock_db.fetch_data.assert_called_once()
        mock_db.save_data.assert_called_once()
