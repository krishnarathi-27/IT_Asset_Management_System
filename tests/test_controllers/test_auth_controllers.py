# from unittest import mock, TestCase
# from src.controllers.auth_controllers import AuthControllers

# class TestAuthControllers(TestCase):

#     @classmethod
#     @mock.patch('src.controllers.auth_controllers.CommonHelper')
#     @mock.patch('src.controllers.auth_controllers.DatabaseHelper')
#     def setUpClass(cls, mock_cls, mock_cls1) -> None:
#         cls.db_obj = mock_cls()
#         cls.common_obj = mock_cls1()
#         cls.auth_controller_obj = AuthControllers()

#     def test_first_login_positive(self):
#         self.common_obj.change_default_password.return_value = None
#         self.assertTrue(self.auth_controller_obj.valid_first_login("krishna","krish@123","krish@123"))

#     def test_first_login_negative(self):
#         self.assertFalse(self.auth_controller_obj.valid_first_login("krishna","krish123","krish@123"))

#     @mock.patch('src.controllers.auth_controllers.EmployeeViews')
#     @mock.patch('src.controllers.auth_controllers.ManagerViews')
#     @mock.patch('src.controllers.auth_controllers.AdminViews')
#     def test_role_based_access_positive(self,mock_obj1,mock_obj2,mock_obj3):
#         mock_obj1().admin_operations.return_value = True
#         mock_obj2().manager_operations.return_value = True
#         mock_obj3().employee_operations.return_value = True
#         self.assertTrue(self.auth_controller_obj.role_based_access("admin","EMP7hyd"))
#         self.assertTrue(self.auth_controller_obj.role_based_access("employee","EMP7hyd"))
#         self.assertTrue(self.auth_controller_obj.role_based_access("asset manager","EMP7hyd"))

#     def test_role_based_access_negative(self):
#         self.assertFalse(self.auth_controller_obj.role_based_access("sd","EMP3rds"))

#     def validate_user(self):
#         pass