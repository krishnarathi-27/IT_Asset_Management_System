# from unittest import mock, TestCase
# from src.views.employee_views import EmployeeViews


# class TestEmployeeViews(TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.employee_views_obj = EmployeeViews("USN4rww")

#     @mock.patch("src.views.employee_views.EmployeeViews.employee_menu")
#     def test_employee_operations_positive(self, mock_employee_menu) -> bool:
#         mock_employee_menu.return_value = True
#         self.assertIsNone(self.employee_views_obj.employee_menu_operations())
#         mock_employee_menu.assert_called_once()

#     @mock.patch("src.views.employee_views.EmployeeViews.employee_menu")
#     def test_employee_operations_negative(self, mock_employee_menu) -> bool:
#         mock_employee_menu.side_effect = [False, True]
#         self.assertIsNone(self.employee_views_obj.employee_menu_operations())
#         self.assertEqual(mock_employee_menu.call_count, 2)

#     @mock.patch("src.views.employee_views.EmployeeViews.input_raise_issue")
#     @mock.patch("src.views.employee_views.EmployeeViews.check_assets_assigned")
#     @mock.patch("src.views.employee_views.EmployeeViews.display_details")
#     @mock.patch("builtins.input")
#     def test_employee_menu_negative(
#         self, mock_input, mock_case_1, mock_case_2, mock_case_3
#     ) -> bool:
#         mock_input.side_effect = ["1", "2", "3", "sw"]
#         for _ in range(4):
#             self.assertFalse(self.employee_views_obj.employee_menu())
#         mock_case_1.assert_called_once()
#         mock_case_2.assert_called_once()
#         mock_case_3.assert_called_once()

#     @mock.patch("builtins.input")
#     def test_employee_menu_positive(self, mock_input) -> bool:
#         mock_input.return_value = "4"
#         self.assertTrue(self.employee_views_obj.employee_menu())
