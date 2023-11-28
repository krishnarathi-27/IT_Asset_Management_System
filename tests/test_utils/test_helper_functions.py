from src.utils.helper_functions import HelperFunctions

class TestHelperFunctions:

    def test_positive_is_category(self,monkeypatch):
        monkeypatch.setattr('src.utils.helper_functions.db.fetch_data', lambda a,b:True)
        assert HelperFunctions.is_category("CATcde3") == True

    def test_negative_is_category(self,monkeypatch):
        monkeypatch.setattr('src.utils.helper_functions.db.fetch_data', lambda a,b:False)
        assert HelperFunctions.is_category("dtch") == False

    def test_positive_is_asset(self,monkeypatch):
        monkeypatch.setattr('src.utils.helper_functions.db.fetch_data', lambda a,b:True)
        assert HelperFunctions.is_asset("ASN7hd3") == True

    def test_negative_is_asset(self,monkeypatch):
        monkeypatch.setattr('src.utils.helper_functions.db.fetch_data', lambda a,b:False)
        assert HelperFunctions.is_asset("dtch") == False

    def test_positive_is_user(self,monkeypatch):
        monkeypatch.setattr('src.utils.helper_functions.db.fetch_data', lambda a,b:True)
        assert HelperFunctions.is_user("EMP09uh") == True

    def test_negative_is_user(self,monkeypatch):
        monkeypatch.setattr('src.utils.helper_functions.db.fetch_data', lambda a,b:False)
        assert HelperFunctions.is_user("usexe") == False

    def test_positive_is_vendor(self,monkeypatch):
        monkeypatch.setattr('src.utils.helper_functions.db.fetch_data', lambda a,b:True)
        assert HelperFunctions.is_vendor("VENde9f") == True

    def test_negative_is_vendor(self,monkeypatch):
        monkeypatch.setattr('src.utils.helper_functions.db.fetch_data', lambda a,b:False)
        assert HelperFunctions.is_vendor("swdece") == False