from unittest import mock, TestCase

class TestAuthViews(TestCase):

    @classmethod
    def setUp(cls):
        cls.login_attempts = 3
        cls.auth_controller_obj = mock.Mock()

    def test_login(self):
        pass