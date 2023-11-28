from unittest import TestCase, mock
import pytest
from src.admin.admin_actions import AdminActions
from src.config.statements.statements import StatementsConfig

@pytest.fixture(scope="class")
def admin_obj():
    obj = AdminActions()
    yield obj
    del obj

class TestAdminActions:

    @pytest.mark.parametrize("test_data",[(("san","1","2"),("asset manager","employee"))])
    def test_select_user_role(self,monkeypatch,test_data,admin_obj):
        inp = iter(test_data[0])
        expected = iter(test_data[1])
        monkeypatch.setattr('builtins.input',lambda _: next(inp))
        monkeypatch.setattr(StatementsConfig,'asset_manager',value='asset manager')
        monkeypatch.setattr(StatementsConfig,'employee', value='employee')
        assert admin_obj.select_user_role() == next(expected)

#     def test_create_user_role(self,monkeypatch):
#         monkeypatch.setattr('shortuuid.ShortUUID',lambda : '')

# class TestAdminActions(TestCase):

#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.obj = AdminActions()

#     @classmethod
#     def tearDownClass(cls) -> None:
#         del cls.obj

#     def test_select_user_role(self)