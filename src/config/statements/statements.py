import yaml

FILE_PATH = "src\\config\\statements\\statements_file.yml"

class StatementsConfig:
    
    starting_application = None
    invalid_input = None
    enter_vendor_email = None
    vendor_not_exists = None
    user_not_exists = None
    administrator = None
    asset_manager = None
    employee = None
    no_data_exists = None
    enter_assetid = None
    assetid_not_exists = None
    enter_user_id = None
    enter_category_id = None
    category_id_not_exists = None
    select_from_table = None
    enter_vendor_id = None
    enter_maintenance_id = None
    enter_mapping_id = None
    enter_issue_id = None
    mapping_id_not_exists = None
    category_added = None
    category_vendor_exists = None
    enter_category_name = None
    enter_brand_name = None
    max_login_attempts = None
    database_location = None
    assignable_asset_type = None
    unassignable_asset_type = None
    unavailable_status = None
    available_status = None
    asset_location = None
    regex_user_id = None
    regex_asset_id = None
    regex_category_id = None
    regex_mapping_id = None
    regex_vendor_id = None
    regex_issue_id = None
    regex_maintenance_id = None
    regex_name = None
    regex_password = None
    regex_email = None
    date_format = None
    invalid_login = None
    input_default_password = None
    input_new_password = None
    input_confirm_password = None
    password_not_match = None
    default_password_updated = None
    provide_role_based_access = None
    attempts_message = None
    attempts_exhausted = None
    enter_username = None
    enter_password = None
    strong_password = None
    login_again = None
    wait_for_login = None
    welcome_admin = None
    deleted_vendor = None
    username_exists = None
    user_added_success = None
    user_deleted_success = None
    vendor_not_exist_to_delete = None
    issue_raised = None
    welcome_employee = None
    welcome_manager = None
    input_vendor_email = None
    input_vendor_name = None
    vendor_added = None
    input_purchased_date = None
    asset_added_success = None
    assign_asset_statement = None
    asset_assign_success = None
    unassign_asset_statement = None
    unassign_asset_success = None
    send_for_maintenance = None
    recieve_from_maintenance = None
    exception_message = None

    @classmethod
    def load(cls):
        with open(FILE_PATH,'r') as file:
            data = yaml.safe_load(file)

            #main file
            cls.starting_application = data['starting_application']

            #common
            cls.invalid_input = data['invalid_input']
            cls.enter_vendor_email = data['enter_vendor_email']
            cls.vendor_not_exists = data['vendor_not_exists']
            cls.user_not_exists = data['user_not_exists']
            cls.administrator = data['administrator']
            cls.asset_manager = data['asset_manager']
            cls.employee = data['employee']
            cls.no_data_exists = data['no_data_exists']
            cls.enter_assetid = data['enter_assetid']
            cls.assetid_not_exists = data['assetid_not_exists']
            cls.enter_user_id = data['enter_user_id']
            cls.enter_category_id = data['enter_category_id']
            cls.category_id_not_exists = data['category_id_not_exists']
            cls.select_from_table = data['select_from_table']
            cls.enter_vendor_id = data['enter_vendor_id']
            cls.enter_maintenance_id = data['enter_maintenance_id']
            cls.enter_mapping_id = data['enter_mapping_id']
            cls.enter_issue_id = data['enter_issue_id']
            cls.mapping_id_not_exists = data['mapping_id_not_exists']
            cls.category_added = data['category_added']
            cls.category_vendor_exists = data['category_vendor_exists']
            cls.enter_category_name = data['enter_category_name']
            cls.enter_brand_name = data['enter_brand_name']

            #constants
            cls.max_login_attempts = data['max_login_attempts']
            cls.database_location = data['database_location']
            cls.assignable_asset_type = data['assignable_asset_type']
            cls.unassignable_asset_type = data['unassignable_asset_type']
            cls.unavailable_status = data['unavailable_status']
            cls.available_status = data['available_status']
            cls.asset_location = data['asset_location']
            cls.regex_user_id = data['regex_user_id']
            cls.regex_asset_id = data['regex_asset_id']
            cls.regex_category_id = data['regex_category_id']
            cls.regex_mapping_id = data['regex_mapping_id']
            cls.regex_vendor_id = data['regex_vendor_id']
            cls.regex_issue_id = data['regex_issue_id']
            cls.regex_maintenance_id = data['regex_maintenance_id']
            cls.regex_name = data['regex_name']
            cls.regex_password = data['regex_password']
            cls.regex_email = data['regex_email']
            cls.date_format = data['date_format']

            #authentication
            cls.invalid_login = data['invalid_login']
            cls.input_default_password = data['input_default_password']
            cls.input_new_password = data['input_new_password']
            cls.input_confirm_password = data['input_confirm_password']
            cls.password_not_match = data['password_not_match']
            cls.default_password_updated = data['default_password_updated']
            cls.provide_role_based_access = data['provide_role_based_access']
            cls.attempts_message = data['attempts_message']
            cls.attempts_exhausted = data['attempts_exhausted']
            cls.enter_username = data['enter_username']
            cls.enter_password = data['enter_password']
            cls.strong_password = data['strong_password']
            cls.login_again = data['login_again']
            cls.wait_for_login = data['wait_for_login']

            #admin
            cls.welcome_admin = data['welcome_admin']
            cls.deleted_vendor = data['deleted_vendor']
            cls.username_exists = data['username_exists']
            cls.user_added_success = data['user_added_success']
            cls.user_deleted_success = data['user_deleted_success']
            cls.vendor_not_exist_to_delete = data['vendor_not_exist_to_delete']

            #employee
            cls.issue_raised = data['issue_raised']
            cls.welcome_employee = data['welcome_employee']

            #manager
            cls.welcome_manager = data['welcome_manager']
            cls.input_vendor_email = data['input_vendor_email']
            cls.input_vendor_name = data['input_vendor_name']
            cls.vendor_added = data['vendor_added']
            cls.input_purchased_date = data['input_purchased_date']
            cls.asset_added_success = data['asset_added_success']
            cls.assign_asset_statement = data['assign_asset_statement']
            cls.asset_assign_success = data['asset_assign_success']
            cls.unassign_asset_statement = data['unassign_asset_statement']
            cls.unassign_asset_success = data['unassign_asset_success']
            cls.send_for_maintenance = data['send_for_maintenance']
            cls.recieve_from_maintenance = data['recieve_from_maintenance']

            #database
            cls.exception_message = data['exception_message']