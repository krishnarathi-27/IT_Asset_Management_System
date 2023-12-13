from unittest import mock, TestCase
from src.views.maintenance_views import MaintenanceViews


class TestMaintenanceViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.maintenance_views_obj = MaintenanceViews("USN4rww")

    @mock.patch("src.views.maintenance_views.MaintenanceViews.maintenance_menu")
    def test_maintenance_operations_positive(self, mock_maintenance_menu) -> bool:
        mock_maintenance_menu.return_value = True
        self.assertIsNone(self.maintenance_views_obj.maintenance_menu_operations())
        mock_maintenance_menu.assert_called_once()

    @mock.patch("src.views.maintenance_views.MaintenanceViews.maintenance_menu")
    def test_maintenance_operations_negative(self, mock_maintenance_menu) -> bool:
        mock_maintenance_menu.side_effect = [False, True]
        self.assertIsNone(self.maintenance_views_obj.maintenance_menu_operations())
        self.assertEqual(mock_maintenance_menu.call_count, 2)

    @mock.patch("src.views.maintenance_views.MaintenanceViews.input_recieve_asset")
    @mock.patch("src.views.maintenance_views.MaintenanceViews.input_send_asset")
    @mock.patch("src.views.maintenance_views.MaintenanceViews.display_issues")
    @mock.patch("builtins.input")
    def test_maintenance_menu_negative(
        self, mock_input, mock_case_1, mock_case_2, mock_case_3
    ) -> bool:
        mock_input.side_effect = ["1", "2", "3", "dew"]
        for _ in range(4):
            self.assertFalse(self.maintenance_views_obj.maintenance_menu())
        mock_case_1.assert_called_once()
        mock_case_2.assert_called_once()
        mock_case_3.assert_called_once()

    @mock.patch("builtins.input")
    def test_maintenance_menu_positive(self, mock_input) -> bool:
        mock_input.return_value = "4"
        self.assertTrue(self.maintenance_views_obj.maintenance_menu())
