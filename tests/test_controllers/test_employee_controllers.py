from unittest import TestCase, mock
from src.controllers.employee_controllers import EmployeeControllers


class TestAssetDataController(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_controller_obj = EmployeeControllers()

    @mock.patch("src.controllers.employee_controllers.db")
    def test_display_employee_details_positive(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertTrue(self.emp_controller_obj.display_employee_details("sde"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.employee_controllers.db")
    def test_display_employee_details_negative(self, mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.emp_controller_obj.display_employee_details("sde"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.employee_controllers.db")
    def test_display_assets_assigned_positive(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        self.assertTrue(self.emp_controller_obj.display_assets_assigned("sde"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.employee_controllers.db")
    def test_display_assets_assigned_negative(self, mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.emp_controller_obj.display_assets_assigned("sde"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.employee_controllers.db")
    def test_raise_issue_positive(self, mock_db):
        mock_db.fetch_data.return_value = ["data"]
        mock_db.save_data.return_value = None
        self.assertTrue(self.emp_controller_obj.raise_issue("sud", "sd"))
        mock_db.fetch_data.assert_called_once()
        mock_db.save_data.assert_called_once()

    @mock.patch("src.controllers.employee_controllers.db")
    def test_raise_issue_negative(self, mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.emp_controller_obj.raise_issue("sud", "sd"))
        mock_db.fetch_data.assert_called_once()
