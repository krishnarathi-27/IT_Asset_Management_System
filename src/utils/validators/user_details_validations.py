import re
import maskpass
from config.statements.statements import StatementsConfig

class UserDetailsValidations:
    
    @staticmethod
    def input_name() -> str:
        while True:
            name = input(StatementsConfig.enter_username).strip().lower()
            if re.match(StatementsConfig.regex_name,name):
                return name
            print(StatementsConfig.invalid_input)

    @staticmethod
    def input_email() -> str:
        while True:
            email = input(StatementsConfig.enter_vendor_email).strip()
            if re.match(StatementsConfig.regex_email,email):
                return email
            print(StatementsConfig.invalid_input)

    @staticmethod
    def input_password() -> str:
        while True:
            password = maskpass.askpass(StatementsConfig.enter_password).strip()
            if re.match(StatementsConfig.regex_password,password):
                return password
            print(StatementsConfig.invalid_input)
