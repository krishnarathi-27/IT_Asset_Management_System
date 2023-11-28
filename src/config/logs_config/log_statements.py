import yaml

FILE_PATH  = "src\\config\\logs_config\\log_statements.yml"

class LogStatements:

    log_file_location = None
    category_added = None
    vendor_added = None
    starting_application_log = None
    invalid_login_log = None
    default_pwd_updated_log = None
    log_create_new_user = None
    log_delete_new_user = None
    log_admin_logged_in = None
    log_vendor_deactivated = None
    log_error_connecting_database = None
    issue_raised = None
    employee_logged_in = None
    manager_logged_in = None
    asset_added = None
    asigned_assets = None
    unassigned_asset = None
    
    @classmethod
    def load(cls):
        with open(FILE_PATH,'r') as file:
            data = yaml.safe_load(file)
            #main
            cls.log_file_location = data['log_file_location']

            #common
            cls.category_added = data['category_added']
            cls.vendor_added = data['vendor_added']

            #authentication logs
            cls.starting_application_log = data['starting_application_log']
            cls.invalid_login_log = data['invalid_login_log']
            cls.default_pwd_updated_log = data['default_pwd_updated_log']

            #admin
            cls.log_create_new_user = data['log_create_new_user']
            cls.log_delete_new_user = data['log_delete_new_user']
            cls.log_admin_logged_in = data['log_admin_logged_in']
            cls.log_vendor_deactivated = data['log_vendor_deactivated']
            
            #database
            cls.log_error_connecting_database = data['log_error_connecting_database']

            #employee
            cls.issue_raised = data['issue_raised']
            cls.employee_logged_in = data['employee_logged_in']

            #manager
            cls.manager_logged_in = data['manager_logged_in']
            cls.asset_added = data['asset_added']
            cls.asigned_assets = data['asigned_assets']
            cls.unassigned_asset = data['unassigned_asset']