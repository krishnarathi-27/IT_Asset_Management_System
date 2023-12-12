from unittest import mock, TestCase
from src.views.admin_views import AdminViews

class TestAdminViews(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.admin_views_obj = AdminViews()

    @mock.patch('src.views.admin_views.AdminViews.admin_menu')
    def test_admin_operations_positive(self, mock_admin_menu) -> bool:
        mock_admin_menu.return_value = True
        self.assertIsNone(self.admin_views_obj.admin_operations())
        mock_admin_menu.assert_called_once()

    @mock.patch('src.views.admin_views.AdminViews.admin_menu')
    def test_admin_operations_negative(self, mock_admin_menu) -> bool:
        mock_admin_menu.side_effect = [False, True]
        self.assertIsNone(self.admin_views_obj.admin_operations())
        self.assertEqual(mock_admin_menu.call_count, 2)

    @mock.patch('src.views.admin_views.AdminViews.check_category_created')
    @mock.patch('src.views.admin_views.AdminViews.display_category')
    @mock.patch('src.views.admin_views.AdminViews.check_vendor_created')
    @mock.patch('src.views.admin_views.AdminViews.check_deactivate_vendor')
    @mock.patch('src.views.admin_views.AdminViews.display_vendors')
    @mock.patch('src.views.admin_views.AdminViews.create_user')
    @mock.patch('src.views.admin_views.CommonHelper.display_user_details')
    @mock.patch('builtins.input')
    def test_admin_menu_negative(self, mock_input, mock_case_1, mock_case_2, mock_case_3, mock_case_4, mock_case_5, mock_case_6, mock_case_7) -> bool:
        mock_input.side_effect = ['1', '2', '3', '4', '5', '6', '7']
        for _ in range(7):
            self.assertFalse(self.admin_views_obj.admin_menu())
        mock_case_1.assert_called_once()
        mock_case_2.assert_called_once()
        mock_case_3.assert_called_once()
        mock_case_4.assert_called_once()
        mock_case_5.assert_called_once()
        mock_case_6.assert_called_once()
        mock_case_7.assert_called_once()

    @mock.patch('builtins.input')
    def test_admin_menu_positive(self, mock_input) -> bool:
        mock_input.return_value = '8'
        self.assertTrue(self.admin_views_obj.admin_menu())