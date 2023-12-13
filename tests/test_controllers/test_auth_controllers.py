from unittest import mock, TestCase
from src.controllers.auth_controllers import AuthControllers


class TestAuthControllers(TestCase):
    @classmethod
    @mock.patch("src.controllers.auth_controllers.CommonHelper")
    def setUpClass(cls, mock_common_helper) -> None:
        cls.mock_obj_common = mock_common_helper()
        cls.auth_controller_obj = AuthControllers()

    def test_valid_first_login_positive(self) -> None:
        self.mock_obj_common.change_default_password.return_value = None
        self.assertTrue(
            self.auth_controller_obj.valid_first_login("name", "pwd", "pwd")
        )
        self.mock_obj_common.change_default_password.assert_called_once()

    def test_valid_first_login_negative(self) -> None:
        self.assertFalse(
            self.auth_controller_obj.valid_first_login("name", "pw1d", "pwd")
        )

    @mock.patch("src.controllers.auth_controllers.EmployeeViews")
    @mock.patch("src.controllers.auth_controllers.ManagerViews")
    @mock.patch("src.controllers.auth_controllers.AdminViews")
    def test_role_based_access_positive(self, mock_obj1, mock_obj2, mock_obj3):
        mock_obj1().admin_operations.return_value = True
        mock_obj2().manager_operations.return_value = True
        mock_obj3().employee_operations.return_value = True
        self.assertTrue(self.auth_controller_obj.role_based_access("admin", "EMP7hyd"))
        self.assertTrue(
            self.auth_controller_obj.role_based_access("employee", "EMP7hyd")
        )
        self.assertTrue(
            self.auth_controller_obj.role_based_access("asset manager", "EMP7hyd")
        )

    def test_role_based_access_negative(self):
        self.assertFalse(self.auth_controller_obj.role_based_access("sd", "EMP3rds"))

    @mock.patch("src.controllers.auth_controllers.db")
    def test_validate_user_negative(self, mock_db):
        mock_db.fetch_data.return_value = []
        self.assertFalse(self.auth_controller_obj.validate_user("name", "pwd"))
        mock_db.fetch_data.assert_called_once()

    @mock.patch("src.controllers.auth_controllers.AuthControllers.role_based_access")
    @mock.patch("src.controllers.auth_controllers.AuthControllers.valid_first_login")
    @mock.patch("src.controllers.auth_controllers.hashlib.sha256")
    @mock.patch("src.controllers.auth_controllers.db")
    def test_validate_user_positive(
        self, mock_db, mock_hashlib, mock_cls_obj1, mock_cls_obj2
    ):
        mock_db.fetch_data.side_effect = [
            [("EMPdsse", "User@1234", "admin", "true")],
            [("EMPdsse", "User@1234", "admin", "false")],
        ]
        mock_hashlib().hexdigest.return_value = "User@1234"
        mock_cls_obj1.return_value = True
        mock_cls_obj2.return_value = True
        self.assertTrue(self.auth_controller_obj.validate_user("name", "pwd"))
        self.assertTrue(self.auth_controller_obj.validate_user("name", "User@1234"))
