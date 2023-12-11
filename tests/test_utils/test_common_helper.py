from unittest import TestCase, mock
from src.utils.common_helper import CommonHelper

class TestInputValidations(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.common_obj = CommonHelper()

    @mock.patch('src.utils.common_helper.db')
    @mock.patch('src.utils.common_helper.hashlib.sha256')
    @mock.patch('src.utils.common_helper.InputValidations.input_password')
    def test_change_default_password_positive(self,mock_input_validations,mock_hashlib,mock_db) -> None:
        mock_input_validations.side_effect = ["Krishna1","Krishna@1","Krishna@1","Krishna@1"]
        mock_hashlib().hexdigest.return_value = "1"
        mock_db.save_data.return_value = True
        self.assertIsNone(self.common_obj.change_default_password("krishna"))
        mock_db.save_data.assert_called_once()

    @mock.patch('src.utils.common_helper.db')
    def test_display_user_details_negative(self,mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.common_obj.display_user_details())
        mock_db.fetch_data.assert_called_once()

    @mock.patch('src.utils.common_helper.db')
    @mock.patch('src.utils.common_helper.CommonHelper.display_table')
    def test_display_user_details_positive(self,mock_common_helper,mock_db): 
        mock_common_helper.return_value = "naman"
        mock_db.fetch_data.return_value = True
        self.assertTrue(self.common_obj.display_user_details())
        mock_db.fetch_data.assert_called_once()

    @mock.patch('src.utils.common_helper.InputValidations.input_email')
    @mock.patch('builtins.input')
    def test_input_category_details(self,mock_input,mock_input_validation):
        mock_input.side_effect =["mouse","dell"]
        mock_input_validation.return_value = "krish@gmail.com"
        self.assertEqual(CommonHelper.input_category_details(),("mouse","dell","krish@gmail.com"))
    