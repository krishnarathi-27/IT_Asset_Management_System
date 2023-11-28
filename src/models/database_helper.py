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