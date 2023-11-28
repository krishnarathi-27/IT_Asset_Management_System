import pytest
from src.utils.validators.type_id_validations import TypeIdValidations

class TestTypeIdValidations:

    @pytest.mark.parametrize("userid",[(("","EMPcr6g"),(False,True))])
    def test_input_user_id(self,monkeypatch,userid):
        inp = iter(userid[0])
        expected = iter(userid[1])
        monkeypatch.setattr('builtins.input', lambda _: next(inp))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert TypeIdValidations.input_user_id() == userid[0][-1]

    @pytest.mark.parametrize("asset_id",[(("asne)-","ASNjyh8"),(False,True))])
    def test_input_asset_id(self,monkeypatch,asset_id):
        inp = iter(asset_id[0])
        expected = iter(asset_id[1])
        monkeypatch.setattr('builtins.input', lambda _: next(inp))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert TypeIdValidations.input_asset_id() == asset_id[0][-1]

    @pytest.mark.parametrize("vendor_id",[(("dwefrctg","VEN5t5t"),(False,True))])
    def test_input_vendor_id(self,monkeypatch,vendor_id):
        inp = iter(vendor_id[0])
        expected = iter(vendor_id[1])
        monkeypatch.setattr('builtins.input', lambda _: next(inp))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert TypeIdValidations.input_vendor_id() == vendor_id[0][-1]

    @pytest.mark.parametrize("category_id",[(("","CATfref"),(False,True))])
    def test_input_category_id(self,monkeypatch,category_id):
        inp = iter(category_id[0])
        expected = iter(category_id[1])
        monkeypatch.setattr('builtins.input', lambda _: next(inp))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert TypeIdValidations.input_category_id() == category_id[0][-1]

    @pytest.mark.parametrize("mapping_id",[(("---","","MPN7yg6"),(False,False,True))])
    def test_input_mapping_id(self,monkeypatch,mapping_id):
        inp = iter(mapping_id[0])
        expected = iter(mapping_id[1])
        monkeypatch.setattr('builtins.input', lambda _: next(inp))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert TypeIdValidations.input_mapping_id() == mapping_id[0][-1]

    @pytest.mark.parametrize("issue_id",[(("--","ISNihyg"),(False,True))])
    def test_input_issue_id(self,monkeypatch,issue_id):
        inp = iter(issue_id[0])
        expected = iter(issue_id[1])
        monkeypatch.setattr('builtins.input', lambda _: next(inp))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert TypeIdValidations.input_issue_id() == issue_id[0][-1]

    @pytest.mark.parametrize("maintenance_id",[(("krishna","MTN09jd"),(False,True))])
    def test_input_maintenance_id(self,monkeypatch,maintenance_id):
        inp = iter(maintenance_id[0])
        expected = iter(maintenance_id[1])
        monkeypatch.setattr('builtins.input', lambda _: next(inp))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert TypeIdValidations.input_maintenance_id() == maintenance_id[0][-1]
