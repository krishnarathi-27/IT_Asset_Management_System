# from unittest import mock, TestCase
# from src.views.manager_views import ManagerViews


# class TestManagerViews(TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.manager_views_obj = ManagerViews("EMPdsaw")

#     @mock.patch("src.views.manager_views.ManagerViews.manager_menu")
#     def test_manager_operations_positive(self, mock_manager_menu) -> bool:
#         mock_manager_menu.return_value = True
#         self.assertIsNone(self.manager_views_obj.manager_menu_operations())
#         mock_manager_menu.assert_called_once()

#     @mock.patch("src.views.manager_views.ManagerViews.manager_menu")
#     def test_manager_operations_negative(self, mock_manager_menu) -> bool:
#         mock_manager_menu.side_effect = [False, True]
#         self.assertIsNone(self.manager_views_obj.manager_menu_operations())
#         self.assertEqual(mock_manager_menu.call_count, 2)

#     @mock.patch("src.views.manager_views.MaintenanceViews.maintenance_menu_operations")
#     @mock.patch("src.views.manager_views.TrackAssetViews.track_asset_menu_operations")
#     @mock.patch("src.views.manager_views.AssetViews.check_unassign_asset")
#     @mock.patch("src.views.manager_views.AssetViews.check_assign_asset")
#     @mock.patch("src.views.manager_views.AssetViews.view_asset")
#     @mock.patch("src.views.manager_views.AssetViews.add_asset")
#     @mock.patch("src.views.manager_views.ManagerViews.check_category_created")
#     @mock.patch("src.views.manager_views.ManagerViews.display_category")
#     @mock.patch("src.views.manager_views.ManagerViews.check_vendor_created")
#     @mock.patch("src.views.manager_views.ManagerViews.display_vendors")
#     @mock.patch("src.views.manager_views.CommonHelper.display_user_details")
#     @mock.patch("builtins.input")
#     def test_manager_menu_negative(
#         self,
#         mock_input,
#         mock_case_1,
#         mock_case_2,
#         mock_case_3,
#         mock_case_4,
#         mock_case_5,
#         mock_case_6,
#         mock_case_7,
#         mock_case_8,
#         mock_case_9,
#         mock_case_10,
#         mock_case_11,
#     ) -> bool:
#         mock_input.side_effect = [
#             "1",
#             "2",
#             "3",
#             "4",
#             "5",
#             "6",
#             "7",
#             "8",
#             "9",
#             "10",
#             "11",
#             "2wsxd",
#         ]
#         for _ in range(12):
#             self.assertFalse(self.manager_views_obj.manager_menu())
#         mock_case_1.assert_called_once()
#         mock_case_2.assert_called_once()
#         mock_case_3.assert_called_once()
#         mock_case_4.assert_called_once()
#         mock_case_5.assert_called_once()
#         mock_case_6.assert_called_once()
#         mock_case_7.assert_called_once()
#         mock_case_8.assert_called_once()
#         mock_case_9.assert_called_once()
#         mock_case_10.assert_called_once()
#         mock_case_11.assert_called_once()

#     @mock.patch("builtins.input")
#     def test_manager_menu_positive(self, mock_input) -> bool:
#         mock_input.return_value = "12"
#         self.assertTrue(self.manager_views_obj.manager_menu())
