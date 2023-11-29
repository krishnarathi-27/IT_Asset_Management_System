from unittest import TestCase, mock
from src.utils.common_helper import CommonHelper

class TestInputValidations(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.db_obj = mock.Mock()
        cls.common_obj = CommonHelper()

    @mock.patch('src.utils.common_helper.DatabaseHelper.update_default_password')
    @mock.patch('hashlib.sha256')
    @mock.patch('src.utils.common_helper.InputValidations.input_password')
    def test_change_default_password(self,mock_input_validations,mock_hashlib,mock_db_helper) -> None:
        mock_input_validations.side_effect = ["Krishna@1","Krihsns2q@1","Krishna@1","Krishna@1"]
        mock_hashlib.hexdigest.return_value = "1"
        mock_db_helper.return_value = True
        self.assertEqual(self.common_obj.change_default_password("krishna"),None)


    @mock.patch('src.utils.common_helper.CommonHelper.display_table')
    @mock.patch('src.utils.common_helper.DatabaseHelper.get_user_details')
    def test_display_user_details(self,mock_common_helper,mock_db_helper): 
        mock_common_helper.side_effect = [[],["naman"]]
        mock_db_helper.return_value = True
        self.assertFalse(self.common_obj.display_user_details())
        self.assertTrue(self.common_obj.display_user_details())

    @mock.patch('src.utils.common_helper.InputValidations.input_email')
    @mock.patch('builtins.input')
    def test_input_category_details(self,mock_input,mock_input_validation):
        mock_input.side_effect =["mouse","dell"]
        mock_input_validation.return_value = "krish@gmail.com"
        self.assertEqual(CommonHelper.input_category_details(),("mouse","dell","krish@gmail.com"))
    