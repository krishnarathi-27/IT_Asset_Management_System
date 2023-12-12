import sqlite3
from unittest import TestCase, mock
from src.utils.app_decorator import error_handler

class TestErrorHandler(TestCase):

    def test_error_handler_positive(self) -> bool:
        demo_func = mock.Mock(name = 'demo_func')
        demo_func.return_value = "Decorator tested"
        wrapped = error_handler(demo_func)
        self.assertEqual(wrapped(), "Decorator tested")

    def test_error_handler_negative(self) -> bool:
        demo_func = mock.Mock(name = 'demo_func')
        demo_func.side_effect = [ sqlite3.IntegrityError, sqlite3.OperationalError,
                        sqlite3.ProgrammingError, sqlite3.Error,
                        ValueError, TypeError, Exception
                    ]
        wrapped = error_handler(demo_func)
        for _ in range(7):
            self.assertIsNone(wrapped())