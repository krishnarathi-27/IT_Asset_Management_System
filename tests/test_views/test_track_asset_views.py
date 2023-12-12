from unittest import mock, TestCase
from src.views.track_asset_views import TrackAssetViews

class TestTrackAssetViews(TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.track_asset_views_obj = TrackAssetViews()

    @mock.patch('src.views.track_asset_views.TrackAssetViews.track_asset_menu')
    def test_track_asset_operations_positive(self, mock_track_asset_menu) -> bool:
        mock_track_asset_menu.return_value = True
        self.assertIsNone(self.track_asset_views_obj.track_asset_operations())
        mock_track_asset_menu.assert_called_once()

    @mock.patch('src.views.track_asset_views.TrackAssetViews.track_asset_menu')
    def test_track_asset_operations_negative(self, mock_track_asset_menu) -> bool:
        mock_track_asset_menu.side_effect = [False, True]
        self.assertIsNone(self.track_asset_views_obj.track_asset_operations())
        self.assertEqual(mock_track_asset_menu.call_count, 2)

    @mock.patch('src.views.track_asset_views.TrackAssetViews.track_asset_maintenance')
    @mock.patch('src.views.track_asset_views.TrackAssetViews.track_asset_available')
    @mock.patch('src.views.track_asset_views.TrackAssetViews.track_input_vendor')
    @mock.patch('src.views.track_asset_views.TrackAssetViews.track_input_category')
    @mock.patch('src.views.track_asset_views.TrackAssetViews.track_input_username')
    @mock.patch('builtins.input')
    def test_track_asset_menu_negative(self, mock_input, mock_case_1, mock_case_2, mock_case_3, mock_case_4, mock_case_5) -> bool:
        mock_input.side_effect = ['1', '2', '3','4','5']
        for _ in range(5):
            self.assertFalse(self.track_asset_views_obj.track_asset_menu())
        mock_case_1.assert_called_once()
        mock_case_2.assert_called_once()
        mock_case_3.assert_called_once()
        mock_case_4.assert_called_once()
        mock_case_5.assert_called_once()

    @mock.patch('builtins.input')
    def test_track_asset_menu_positive(self, mock_input) -> bool:
        mock_input.return_value = '6'
        self.assertTrue(self.track_asset_views_obj.track_asset_menu())