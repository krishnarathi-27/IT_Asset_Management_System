from unittest import mock, TestCase
from src.views.admin_views import AdminViews


class TestAdminViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.admin_views_obj = AdminViews()

#     @mock.patch("src.views.admin_views.AdminViews.check_category_created")
#     @mock.patch("src.views.admin_views.AdminViews.display_category")
#     @mock.patch("src.views.admin_views.AdminViews.check_vendor_created")
#     @mock.patch("src.views.admin_views.AdminViews.check_deactivate_vendor")
#     @mock.patch("src.views.admin_views.AdminViews.display_vendors")
#     @mock.patch("src.views.admin_views.AdminViews.create_user")
#     @mock.patch("src.views.admin_views.CommonHelper.display_user_details")
#     @mock.patch("builtins.input")
#     def test_admin_menu_operations_negative(
#         self,
#         mock_input,
#         mock_case_1,
#         mock_case_2,
#         mock_case_3,
#         mock_case_4,
#         mock_case_5,
#         mock_case_6,
#         mock_case_7,
#     ) -> bool:
#         mock_input.side_effect = ["1", "2", "3", "4", "5", "6", "7","se"]
#         for _ in range(8):
#             self.assertFalse(self.admin_views_obj.admin_menu_operations())
#         mock_case_1.assert_called_once()
#         mock_case_2.assert_called_once()
#         mock_case_3.assert_called_once()
#         mock_case_4.assert_called_once()
#         mock_case_5.assert_called_once()
#         mock_case_6.assert_called_once()
#         mock_case_7.assert_called_once()

#     @mock.patch("builtins.input")
#     def test_admin_menu_operations_positive(self, mock_input) -> bool:
#         mock_input.return_value = "8"
#         self.assertTrue(self.admin_views_obj.admin_menu_operations())

    @mock.patch("src.views.admin_views.AdminControllers.create_new_user")
    @mock.patch("builtins.input")
    @mock.patch("src.views.admin_views.InputValidations")
    def test_create_user(self, mock_input_validation, mock_input, mock_create_new_user):
        mock_input_validation.input_name.return_value = "krishna"
        mock_input_validation.input_password.return_value = "Krishna@12"
        mock_input.side_effect = ["xdc", "1", "2"]
        self.assertIsNone(self.admin_views_obj.create_user())
        self.assertIsNone(self.admin_views_obj.create_user())
        self.assertEqual(mock_create_new_user.call_count, 2)
