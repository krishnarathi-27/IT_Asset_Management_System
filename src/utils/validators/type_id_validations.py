import re
from datetime import datetime
from config.statements.statements import StatementsConfig

class TypeIdValidations:

    @staticmethod
    def input_user_id() -> str:
        while True:
            user_id = input(StatementsConfig.enter_user_id).strip()
            if re.match(StatementsConfig.regex_user_id,user_id):
                return user_id
            print(StatementsConfig.invalid_input)

    @staticmethod
    def input_asset_id() -> str:
       while True:
           asset_id = input(StatementsConfig.enter_assetid).strip()
           if re.match(StatementsConfig.regex_asset_id,asset_id):
               return asset_id
           print(StatementsConfig.invalid_input)

    @staticmethod
    def input_vendor_id():
        while True:
            vendor_id = input(StatementsConfig.enter_vendor_id).strip()
            if re.match(StatementsConfig.regex_vendor_id,vendor_id):
                return vendor_id
            print(StatementsConfig.invalid_input)

    @staticmethod
    def input_category_id():
        while True:
            vendor_id = input(StatementsConfig.enter_category_id).strip()
            if re.match(StatementsConfig.regex_category_id,vendor_id):
                return vendor_id
            print(StatementsConfig.invalid_input)

    @staticmethod
    def input_mapping_id():
        while True:
            mapping_id = input(StatementsConfig.enter_mapping_id).strip()
            if re.match(StatementsConfig.regex_mapping_id,mapping_id):
                return mapping_id
            print(StatementsConfig.invalid_input)

    @staticmethod
    def input_issue_id():
        while True:
            issue_id = input(StatementsConfig.enter_issue_id).strip()
            if re.match(StatementsConfig.regex_issue_id, issue_id):
                return issue_id
            print(StatementsConfig.invalid_input)

    @staticmethod
    def input_maintenance_id():
        while True:
            maintenance_id = input(StatementsConfig.enter_maintenance_id).strip()
            if re.match(StatementsConfig.regex_maintenance_id,maintenance_id):
                return maintenance_id
            print(StatementsConfig.invalid_input)

    @staticmethod
    def input_date() -> str:
        while True:
            purchased_date = input(StatementsConfig.input_purchased_date).strip()
            try:
                bool(datetime.strptime(purchased_date, StatementsConfig.date_format))
                break
            except ValueError:
                print(StatementsConfig.invalid_input)