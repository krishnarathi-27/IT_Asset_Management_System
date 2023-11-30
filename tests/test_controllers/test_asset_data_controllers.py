from unittest import TestCase, mock
from src.controllers.asset_data_controllers import AssetDataControllers

class TestAssetDataController(TestCase):

    @classmethod
    @mock.patch('src.controllers.asset_data_controllers.DatabaseHelper')
    def setUpClass(cls, mock_cls) -> None:
        cls.db_helper_obj = mock_cls()
        cls.asset_data_obj = AssetDataControllers()

    # def test_category_vendor_exists_positive(self):
    #     self.db_helper_obj.get_from_mapping_table.return_value = None
    #     self.db_helper_obj.save_data_in_mapping_table.return_value = ["data"]
    #     self.assertEqual(self.asset_data_obj._category_vendor_exists("MPN45rd","CATdf3e","VEN4fdd"),True)

    def test_category_vendor_exists_negative(self):
        self.db_helper_obj.get_from_mapping_table.return_value = []
        self.assertEqual(self.asset_data_obj._category_vendor_exists("MPN45rd","CATdf3e","VEN4fdd"),False)

    # @mock.patch('src.controllers.asset_data_controllers.InputValidations.input_name')
    # @mock.patch('src.controllers.asset_data_controllers.InputValidations.input_email')
    # def test_create_vendor(self):
    #     pass