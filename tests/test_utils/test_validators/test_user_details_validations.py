import pytest
from src.utils.validators.user_details_validations import UserDetailsValidations

class TestUserDetailsValidations:

    @pytest.mark.parametrize("names", [((")))",'---',"krishna"),(False,False,True))])
    def test_input_name(self,monkeypatch,names):
        inp = iter(names[0])
        expected = iter(names[1])
        monkeypatch.setattr('builtins.input', lambda _: next(inp))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert UserDetailsValidations.input_name() == names[0][-1]

    @pytest.mark.parametrize("email",[(("krishna","krishna@gmail.com"),(False,True))])
    def test_input_email(self,monkeypatch,email):
        emails = iter(email[0])
        expected = iter(email[1])
        monkeypatch.setattr('builtins.input', lambda _: next(emails))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert UserDetailsValidations.input_email() == email[0][-1]

    @pytest.mark.parametrize("password",[(("kris","Krishna@12"),(False,True))])
    def test_input_password(self,monkeypatch,password):
        passwords = iter(password[0])
        expected = iter(password[1])
        monkeypatch.setattr('maskpass.askpass', lambda _: next(passwords))
        monkeypatch.setattr('re.match',lambda a,b: next(expected))
        assert UserDetailsValidations.input_password() == password[0][-1]
