from unittest import TestCase, mock
from src.controllers.asset_data_controllers import AssetDataControllers

class TestAssetDataController(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.asset_data_obj = AssetDataControllers()

    @mock.patch('src.controllers.asset_data_controllers.db')
    def test_category_vendor_exists_negative(self,mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertFalse(self.asset_data_obj.category_vendor_exists("MPN45rd","CATdf3e","VEN4fdd"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch('src.controllers.asset_data_controllers.db')
    def test_category_vendor_exists_positive(self,mock_db):
        mock_db.fetch_data.return_value = []
        mock_db.save_data.return_value = None
        self.assertTrue(self.asset_data_obj.category_vendor_exists("MPN45rd","CATdf3e","VEN4fdd"))
        mock_db.fetch_data.assert_called_once()
        mock_db.save_data.assert_called_once()

    @mock.patch('src.controllers.asset_data_controllers.db')
    @mock.patch('src.controllers.asset_data_controllers.CommonHelper.display_table')
    def test_view_vendor_positive(self,mock_obj_common_helper,mock_db):
        mock_db.fetch_data.return_value = ["data"]
        mock_obj_common_helper.return_value = None
        self.assertTrue(self.asset_data_obj.view_vendor())
        mock_db.fetch_data.assert_called_once()

    @mock.patch('src.controllers.asset_data_controllers.db')
    def test_view_vendor_negative(self,mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.asset_data_obj.view_vendor())
        mock_db.fetch_data.assert_called_once()

    @mock.patch('src.controllers.asset_data_controllers.db')
    @mock.patch('src.controllers.asset_data_controllers.CommonHelper.display_table')
    def test_view_category_positive(self,mock_obj_common_helper,mock_db):
        mock_db.fetch_data.return_value = ["data"]
        mock_obj_common_helper.return_value = None
        self.assertTrue(self.asset_data_obj.view_category())
        mock_db.fetch_data.assert_called_once()

    @mock.patch('src.controllers.asset_data_controllers.db')
    def test_view_category_negative(self,mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.asset_data_obj.view_category())
        mock_db.fetch_data.assert_called_once()

    @mock.patch('src.controllers.asset_data_controllers.db')
    def test_create_vendor(self,mock_db) -> None:
        mock_db.save_data.return_value = None
        self.assertEqual(self.asset_data_obj.create_vendor("krish@gmail.com","krish"),None)
        mock_db.save_data.assert_called_once()