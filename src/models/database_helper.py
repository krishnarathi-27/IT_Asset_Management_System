"""Module have all the methods which access db function"""
from models.database import db
from config.queries import Queries

class DatabaseHelper:
    """Class containing methods to interact with database"""

    def get_user_credentials(self,username: str) -> list:
        '''
            Method to fetch user credenetials from database for valid login
            Parameters : self, username
            Return Type : list
        '''
        data = db.fetch_data(
                    Queries.FETCH_USER_CREDENTIALS,
                    (username,)
                )
        return data
    
    def update_default_password(self, data: tuple) -> None:
        '''
            Method to save updated default password in database
            Parameters : self, data
            Return Type : None
        '''       
        db.save_data(
            Queries.UPDATE_DEFAULT_PASSWORD, data
        )

    def get_user_details(self) -> list:
        '''
            Method to fetch user data from database for valid login
            Parameters : self
            Return Type : list
        '''
        data = db.fetch_data(
                        Queries.FETCH_AUTHENTICATION_TABLE
                )
        return data
    
    def save_new_user(self,user_id: str,username: str, hashed_password: str, user_role: str) -> None:
        '''
            Method to save new user data in database
            Parameters : self, user_id, username, hashed_password, user_role
            Return Type : None
        '''
        db.save_data(
            Queries.INSERT_USER_CREDENTIALS,
            (user_id,username,hashed_password,user_role,)
        )

    def get_vendor_details(self) -> list:
        '''
            Method to fetch vendor details from database
            Parameters : self
            Return Type : list
        '''       
        data = db.fetch_data(
                    Queries.FETCH_VENDOR_TABLE
                )
        return data
    
    def update_vendor_active_status(self,vendor_email) -> None:
        '''
            Method to update vendor active status
            Parameters : self, vendor email
            Return Type : list
        '''
        db.save_data(
            Queries.UPDATE_VENDOR_ACTIVE_STATUS,
            (vendor_email,)
        )  

    def get_vendor_by_email(self,vendor_email) -> None:
        """
            Method to fetch vendor details by email
            Parameters : self, vendor_email
            Return Type : None
        """
        data = db.fetch_data(
                    Queries.FETCH_VENDOR_BY_EMAIL,
                    (vendor_email,)
                )
        return data
    
    def save_new_vendor(self,vendor_id: str,vendor_name: str,vendor_email: str) -> None:
        '''
            Method to save new vendor data in database
            Parameters : self, vendor_id, vendor_name, vendor_email
            Return Type : None
        '''       
        db.save_data(
            Queries.INSERT_VENDOR_DETAILS,
            (vendor_id,vendor_name,vendor_email,)
        )

    def get_category_details(self) -> list:
        '''
            Method to fetch category details from database
            Parameters : self
            Return Type : list
        '''       
        data = db.fetch_data(
                    Queries.FETCH_CATEGORY_TABLE
                )
        return data
    
    def get_by_category_and_brand_name(self,category_name: str, brand_name: str) -> list:
        '''
            Method to fetch category details from database by category name and brand namw
            Parameters : self, category_name, brand_name
            Return Type : list
        '''         
        data = db.fetch_data(
                    Queries.FETCH_BY_CATEGORY_AND_BRAND_NAME,
                    (category_name,brand_name,)
                )
        return data
    
    def save_category_mapping_details(self, data1: tuple, data2: tuple) -> None:
        '''
            Method to save category details in category table and mapping details in mapping table
            Parameters : self, data1, data2
            Return Type : None
        '''   
        db.save_data([
                Queries.INSERT_CATEGORY_DETAILS,
                Queries.INSERT_MAPPING_DETAILS
            ],
            [data1, data2]
        )

    def get_from_mapping_table(self,category_id: str, vendor_id: str) -> list:
        '''
            Method to fetch mapping table details from database
            Parameters : self, category_id, vendor_id
            Return Type : list
        '''         
        data = db.fetch_data(
                    Queries.FETCH_FROM_MAPPING_TABLE,
                    (category_id,vendor_id,)
                )
        return data
    
    def save_data_in_mapping_table(self,mapping_id: str,category_id: str,vendor_id: str) -> None:
        '''
            Method to save data in mapping table
            Parameters : self,mapping_id, category_id, vendor_id
            Return Type : None
        '''   
        db.save_data(
            Queries.INSERT_MAPPING_DETAILS,
            (mapping_id,category_id,vendor_id,)
        )

    def get_category_vendor_details(self) -> list:
        '''
            Method to fetch data from caegory and endor table
            Parameters : self
            Return Type : list
        '''      
        data = db.fetch_data(
                    Queries.FETCH_MAPPING_ID
            )
        return data
    
    def get_data_if_mapping_id(self,mapping_id: str) -> list:
        '''
            Method to fetch data from table if mapping id exists
            Parameters : self, mapping_id
            Return Type : list
        '''          
        data = db.fetch_data(
                Queries.FETCH_IF_MAPPING_ID_EXISTS,
                (mapping_id,)
            )
        return data
    
    def save_asset_details(self,asset_id: str,mapping_id: str,asset_type: str,purchased_date: str) -> None:
        '''
            Method to save asset details in asset tabl
            Parameters : self,asset_id,mapping_id,asset_type,purchased_date
            Return Type : None
        ''' 
        db.save_data(
            Queries.INSERY_ASSET_DETAILS,
            (asset_id,mapping_id,asset_type,purchased_date)
        )

    def get_asset_details(self)->list:
        '''
            Method to view asset details in asset table
            Parameters : self
            Return Type : list
        ''' 
        data = db.fetch_data(
                Queries.FETCH_ASSETS_TABLE
            )
        return data
    
    def fetch_assignable_asset(self) -> list:
        '''
            Method to view asset details in asset table that are assignable
            Parameters : self
            Return Type : list
        ''' 
        data = db.fetch_data(
                Queries.FETCH_ASSIGNABLE_ASSETS
            )
        return data
    
    def fetch_asset_exists(self,asset_id: str) -> list:
        '''
            Method to fetch assets of asset_id
            Parameters : self
            Return Type : list
        ''' 
        data = db.fetch_data(
                Queries.FETCH_IF_ASSET_EXISTS,
                (asset_id,)
            )
        return data
    
    def fetch_user_exists(self,user_id: str) -> list:
        '''
            Method to fetch ausers of user_id
            Parameters : self
            Return Type : list
        '''        
        data = db.fetch_data(
                Queries.FETCH_IF_USER_EXISTS,
                (user_id,)
            )
        return data
    
    def save_asset_status(self,assigned_to: str ,asset_status: str, asset_id: str) -> None:
        '''
            Method to save asset_status, assigned_to
            Parameters : self
            Return Type : list
        '''        
        db.save_data(
            Queries.UPDATE_ASSET_STATUS,
            (assigned_to,asset_status,asset_id,)
        )

    def fetch_unassignable_assets(self) -> list:
        '''
            Method to view asset details in asset table that are unassignable
            Parameters : self
            Return Type : list
        '''         
        data = db.fetch_data(
                    Queries.FETCH_ASSIGNED_ASSETS_TO_UNASSIGN
                )
        return data
    
    def fetch_asset_by_userid(self, user_id: str) -> list:
        '''
            Method to fetch asset by user id
            Parameters : self
            Return Type : list
        '''        
        data = db.fetch_data(
                    Queries.FETCH_ASSETS_BY_USER_ID,
                    (user_id,)
            )
        return data
    
    def fetch_category_exists(self,category_id: str) -> list:
        '''
            Method to fetch assets by category_id
            Parameters : self
            Return Type : list
        '''             
        data = db.fetch_data(
                Queries.FETCH_ASSETS_BY_CATEGORY_ID,
                (category_id,)
            )
        return data

    def fetch_vendor_exists(self,vendor_email: str) -> list:
        '''
            Method to fetch assets by vendor_email
            Parameters : self
            Return Type : list
        '''             
        data = db.fetch_data(
                Queries.FETCH_ASSETS_BY_VENDOR_EMAIL,
                (vendor_email,)
            )
        return data
    
    def fetch_asset_available(self) -> list:
        '''
            Method to fetch assets available
            Parameters : self
            Return Type : list
        '''         
        data = db.fetch_data(
                Queries.FETCH_ASSETS_AVAILABLE
            )
        return data
    
    def fetch_asset_maintenance(self) -> list:
        '''
            Method to fetch assets maintenance
            Parameters : self
            Return Type : list
        '''         
        data = db.fetch_data(
                Queries.FETCH_ASSETS_UNDER_MAINTENANCE
            )
        return data
    
    def fetch_pending_issues(self) -> list:
        '''
            Method to fetch pending_issues
            Parameters : self
            Return Type : list
        '''         
        data = db.fetch_data(
                Queries.FETCH_ISSUES_PENDING
            )
        return data
    
    def save_maintenance_status(self, tuple1: tuple,tuple2: tuple,tuple3: tuple) -> None:
        '''
            Method to save maintenance status 
            Parameters : self, tuple1, tuple2, tuple3
            Return Type : None
        ''' 
        db.save_data([
                Queries.UPDATE_ISSUE_STATUS_UNDER_MAINTENANCE,
                Queries.INSERT_IN_MAINTENANCE_TABLE,
                Queries.UPDATE_ASSET_STATUS_UNDER_MAINTENANCE
            ],
            [tuple1, tuple2, tuple3]
        )

    def fetch_asset_by_issueid(self, issue_id: str) -> list:
        '''
            Method to asset by issue id
            Parameters : self, issue_id
            Return Type : list
        '''  
        data = db.fetch_data(
            Queries.FETCH_ASSET_ID_BY_ISSUE_ID,
            (issue_id,)
        )
        return data