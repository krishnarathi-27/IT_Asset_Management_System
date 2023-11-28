import yaml

FILE_PATH = "src\config\queries_config\queries_config.yml"

class ConfigQueries:

    create_authentication_table = None
    create_vendor_table = None
    create_asset_category_table = None
    create_mapping_table = None
    create_asset_table = None
    create_maintenance_table = None
    create_issue_table = None
    delete_vendor_details = None
    delete_user_credentials = None
    update_default_password = None
    update_asset_status = None
    update_issue_status_under_maintenance  = None
    update_asset_status_under_maintenance = None
    update_maintenance_return_date = None
    update_asset_status_again_to_available = None
    fetch_authentication_table = None
    fetch_assets_by_user_id  = None
    fetch_vendor_table = None
    fetch_category_table = None
    fetch_assets_table = None
    fetch_assets_by_category_id = None
    fetch_assets_by_vendor_email = None
    fetch_assets_available = None
    fetch_assets_under_maintenance = None
    fetch_user_credentials = None
    fetch_assigned_assets_by_uid = None
    fetch_category_details = None
    fetch_from_mapping_table = None
    fetch_assignable_assets = None
    fetch_assignable_assets_to_assign = None
    fetch_assigned_assets_to_unassign = None
    fetch_issues_pending = None
    fetch_maintenance_table = None
    fetch_asset_id_by_maintenance_table = None
    fetch_if_category_exists = None
    fetch_if_asset_exists = None
    fetch_if_user_exists = None
    fetch_vendor_by_email = None
    fetch_details_by_uid = None
    fetch_if_user_have_asset = None
    fetch_asset_id_by_issue_id = None
    fetch_by_category_and_brand_name = None
    fetch_mapping_id = None
    fetch_if_mapping_id_exists = None
    insert_vendor_details = None
    insert_category_details = None
    insert_mapping_details = None
    insert_in_maintenance_table = None
    insert_user_credentials = None
    insert_issue_for_asset = None
    insert_asset_details = None
    schema_user_table = None     
    schema_vendor_table = None
    schema_asset_table = None
    schema_category_details_table = None
    schema_maintenance_table = None
    schema_assets_by_user_id = None
    schema_assets_by_category_id = None
    schema_assets_by_vendoremail = None
    schema_assets_to_user = None
    schema_category_table = None
    schema_assignable_asset_details = None
    schema_pending_issues = None
    schema_mapping_category_vendor_table  = None

    @classmethod
    def load(cls):
        with open(FILE_PATH,'r') as file:
            data = yaml.safe_load(file)

            #create table queries
            cls.create_authentication_table = data['create_authentication_table']
            cls.create_vendor_table = data['create_vendor_table']
            cls.create_asset_category_table = data['create_asset_category_table']
            cls.create_mapping_table = data['create_mapping_table']
            cls.create_asset_table = data['create_asset_table']
            cls.create_maintenance_table = data['create_maintenance_table']
            cls.create_issue_table = data['create_issue_table']

            #delete data queries
            cls.delete_vendor_details = data['delete_vendor_details']
            cls.delete_user_credentials = data['delete_user_credentials']

            #update data queries
            cls.update_default_password = data['update_default_password']
            cls.update_asset_status = data['update_asset_status']
            cls.update_issue_status_under_maintenance  = data['update_issue_status_under_maintenance']
            cls.update_asset_status_under_maintenance = data['update_asset_status_under_maintenance']
            cls.update_maintenance_return_date = data['update_maintenance_return_date']
            cls.update_asset_status_again_to_available = data['update_asset_status_again_to_available']

            #fetch data queries
            cls.fetch_authentication_table = data['fetch_authentication_table']
            cls.fetch_assets_by_user_id  = data['fetch_assets_by_user_id']
            cls.fetch_vendor_table = data['fetch_vendor_table']
            cls.fetch_category_table = data['fetch_category_table']
            cls.fetch_assets_table = data['fetch_assets_table']
            cls.fetch_assets_by_category_id = data['fetch_assets_by_category_id']
            cls.fetch_assets_by_vendor_email = data['fetch_assets_by_vendor_email']
            cls.fetch_assets_available = data['fetch_assets_available']
            cls.fetch_assets_under_maintenance = data['fetch_assets_under_maintenance']
            cls.fetch_user_credentials = data['fetch_user_credentials']
            cls.fetch_assigned_assets_by_uid = data['fetch_assigned_assets_by_uid']
            cls.fetch_category_details = data['fetch_category_details']
            cls.fetch_from_mapping_table = data['fetch_from_mapping_table']
            cls.fetch_assignable_assets = data['fetch_assignable_assets']
            cls.fetch_assignable_assets_to_assign = data['fetch_assignable_assets_to_assign']
            cls.fetch_assigned_assets_to_unassign = data['fetch_assigned_assets_to_unassign']
            cls.fetch_issues_pending = data['fetch_issues_pending']
            cls.fetch_maintenance_table = data['fetch_maintenance_table']
            cls.fetch_asset_id_by_maintenance_table = data['fetch_asset_id_by_maintenance_table']

            #fetch data if exists
            cls.fetch_if_category_exists = data['fetch_if_category_exists']
            cls.fetch_if_asset_exists = data['fetch_if_asset_exists']
            cls.fetch_if_user_exists = data['fetch_if_user_exists']
            cls.fetch_vendor_by_email = data['fetch_vendor_by_email']
            cls.fetch_details_by_uid = data['fetch_details_by_uid']
            cls.fetch_if_user_have_asset = data['fetch_if_user_have_asset']
            cls.fetch_asset_id_by_issue_id = data['fetch_asset_id_by_issue_id']
            cls.fetch_by_category_and_brand_name = data['fetch_by_category_and_brand_name']
            cls.fetch_mapping_id = data['fetch_mapping_id']
            cls.fetch_if_mapping_id_exists = data['fetch_if_mapping_id_exists']

            #insert details in table
            cls.insert_vendor_details = data['insert_vendor_details']
            cls.insert_category_details = data['insert_category_details']
            cls.insert_mapping_details = data['insert_mapping_details']
            cls.insert_in_maintenance_table = data['insert_in_maintenance_table']
            cls.insert_user_credentials = data['insert_user_credentials']
            cls.insert_issue_for_asset = data['insert_issue_for_asset']
            cls.insert_asset_details = data['insert_asset_details']

            #lists to show complete table details
            cls.schema_user_table = data['schema_user_table']     
            cls.schema_vendor_table = data['schema_vendor_table']
            cls.schema_asset_table = data['schema_asset_table']
            cls.schema_category_details_table = data['schema_category_details_table']
            cls.schema_maintenance_table = data['schema_maintenance_table']

            #lists to display data for some conditions
            cls.schema_assets_by_user_id = data['schema_assets_by_user_id']
            cls.schema_assets_by_category_id = data['schema_assets_by_category_id']
            cls.schema_assets_by_vendoremail = data['schema_assets_by_vendor_email']
            cls.schema_assets_to_user = data['schema_assets_to_user']
            cls.schema_category_table = data['schema_category_table']
            cls.schema_assignable_asset_details = data['schema_assignable_asset_details']
            cls.schema_pending_issues = data['schema_pending_issues']
            cls.schema_mapping_category_vendor_table  = data['schema_mapping_category_vendor_table']
