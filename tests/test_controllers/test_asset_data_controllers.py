from unittest import TestCase, mock
from src.controllers.asset_data_controllers import AssetDataControllers


class TestAssetDataController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.asset_data_obj = AssetDataControllers()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_check_category_with_vendor_positive(self, mock_db):
        mock_db.fetch_data.return_value = []
        mock_db.save_data.return_value = None
        self.assertTrue(
            self.asset_data_obj.check_category_with_vendor(
                "MPN45rd", "CATdf3e", "VEN4fdd"
            )
        )
        mock_db.fetch_data.assert_called_once()
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_check_category_with_vendor_negative(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertFalse(
            self.asset_data_obj.check_category_with_vendor(
                "MPN45rd", "CATdf3e", "VEN4fdd"
            )
        )
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_check_category_positive(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        mock_db.save_data.return_value = None
        self.assertTrue(self.asset_data_obj.check_category("VENde33", "da", "sa"))
        mock_db.fetch_data.assert_called_once()
        mock_db.save_data.assert_called_once()

    @mock.patch(
        "src.controllers.asset_data_controllers.AssetDataControllers.check_category_with_vendor"
    )
    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_check_category_negative(self, mock_db, mock_check_category_vendor) -> None:
        mock_db.fetch_data.return_value = ["data"]
        mock_check_category_vendor.return_value = True
        self.assertTrue(self.asset_data_obj.check_category("VENde33", "da", "sa"))
        mock_db.fetch_data.assert_called_once()
        mock_check_category_vendor.assert_called_once()

    @mock.patch(
        "src.controllers.asset_data_controllers.AssetDataControllers.check_category"
    )
    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_create_category_positive(self, mock_db, mock_check_category) -> None:
        mock_db.fetch_data.return_value = ["data"]
        mock_check_category.return_value = True
        self.assertTrue(self.asset_data_obj.create_category("as", "as", "as"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_create_category_negative(self, mock_db) -> None:
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.asset_data_obj.create_category("as", "as", "asd"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_create_vendor(self, mock_db) -> None:
        mock_db.save_data.return_value = None
        self.assertEqual(
            self.asset_data_obj.create_vendor("krish@gmail.com", "krish"), None
        )
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_view_vendor_positive(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.asset_data_obj.view_vendor(), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_view_vendor_negative(self, mock_db):
        mock_db.fetch_data.return_value = []
        self.assertEqual(self.asset_data_obj.view_vendor(), [])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_view_category_positive(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertEqual(self.asset_data_obj.view_category(), ["data"])
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.asset_data_controllers.db")
    def test_view_category_negative(self, mock_db):
        mock_db.fetch_data.return_value = []
        self.assertEqual(self.asset_data_obj.view_category(), [])
        mock_db.fetch_data.assert_called_once()
