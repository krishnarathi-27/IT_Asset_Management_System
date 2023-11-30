from unittest import TestCase, mock
from src.utils.common_helper import CommonHelper

class TestInputValidations(TestCase):

    @classmethod
    @mock.patch('src.utils.common_helper.DatabaseHelper')
    def setUpClass(cls, mock_cls) -> None:
        cls.db_obj = mock_cls()
        cls.common_obj = CommonHelper()

    @mock.patch('src.utils.common_helper.hashlib.sha256')
    @mock.patch('src.utils.common_helper.InputValidations.input_password')
    def test_change_default_password_positive(self,mock_input_validations,mock_hashlib) -> None:
        mock_input_validations.side_effect = ["Krishna1","Krishna@1","Krishna@1","Krishna@1"]
        mock_hashlib().hexdigest.return_value = "1"
        self.db_obj.update_default_password.return_value = True
        self.assertIsNone(self.common_obj.change_default_password("krishna"))

    def test_display_user_details_negative(self):
        self.db_obj.get_user_details.return_value = []
        self.assertFalse(self.common_obj.display_user_details())

    @mock.patch('src.utils.common_helper.CommonHelper.display_table')
    def test_display_user_details_positive(self,mock_common_helper): 
        mock_common_helper.return_value = "naman"
        self.db_obj.get_user_details.return_value = True
        self.assertTrue(self.common_obj.display_user_details())

    @mock.patch('src.utils.common_helper.InputValidations.input_email')
    @mock.patch('builtins.input')
    def test_input_category_details(self,mock_input,mock_input_validation):
        mock_input.side_effect =["mouse","dell"]
        mock_input_validation.return_value = "krish@gmail.com"
        self.assertEqual(CommonHelper.input_category_details(),("mouse","dell","krish@gmail.com"))
    