"""This module contains all the queries of the project"""
from config.prompts.prompts import PromptConfig

PromptConfig.load()

class Queries:
    """Queries class is used to load queries"""

    CREATE_DATABASE = 'CREATE DATABASE IF NOT EXISTS {}'
    USE_DATABASE = 'USE {}'

    CREATE_AUTHENTICATION_TABLE = """
        CREATE TABLE IF NOT EXISTS authentication(
            user_id VARCHAR(10) PRIMARY KEY,
            username VARCHAR(30) UNIQUE,
            password VARCHAR(150),
            role VARCHAR(20),
            is_changed VARCHAR(10) DEFAULT "false" 
        )
    """
    CREATE_VENDOR_TABLE = """
        CREATE TABLE IF NOT EXISTS vendor_table(
            vendor_id VARCHAR(10) PRIMARY KEY,
            vendor_name VARCHAR(30),
            vendor_email VARCHAR(50) UNIQUE,
            active_status VARCHAR(10) DEFAULT "true"
        )   
    """
    CREATE_ASSET_CATEGORY_TABLE = """
        CREATE TABLE IF NOT EXISTS asset_category(
            category_id VARCHAR(10) PRIMARY KEY,
            category_name VARCHAR(30),
            brand_name VARCHAR(30),
            UNIQUE(category_name,brand_name)
        )   
    """
    CREATE_MAPPING_TABLE = """
        CREATE TABLE IF NOT EXISTS mapping_table(
            mapping_id VARCHAR(10) PRIMARY KEY,
            category_id VARCHAR(10),
            vendor_id VARCHAR(10),
            FOREIGN KEY(category_id) REFERENCES asset_category(category_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(vendor_id) REFERENCES vendor_table(vendor_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    """
    CREATE_ASSET_TABLE = """
        CREATE TABLE IF NOT EXISTS asset_table(
            asset_id VARCHAR(10) PRIMARY KEY,
            mapping_id VARCHAR(10),
            asset_type VARCHAR(20),
            assigned_to VARCHAR(20) DEFAULT "location",
            asset_status VARCHAR(20) DEFAULT "available",
            FOREIGN KEY(mapping_id) REFERENCES mapping_table(mapping_id) ON DELETE CASCADE ON UPDATE CASCADE
        )    
    """

    CREATE_ISSUE_TABLE = """
        CREATE TABLE IF NOT EXISTS issue_table(
            issue_id VARCHAR(10) PRIMARY KEY,
            user_id VARCHAR(10),
            asset_id VARCHAR(10),
            issue_status VARCHAR(20) DEFAULT "pending",
            issue_resolved_by VARCHAR(20) DEFAULT "pending",
            FOREIGN KEY(asset_id) REFERENCES asset_table(asset_id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY(user_id) REFERENCES authentication(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        )    
    """

    CREATE_TOKEN_TABLE = """
        CREATE TABLE IF NOT EXISTS token_table(
            user_id VARCHAR(10) ,
            access_token VARCHAR(100) UNIQUE NOT NULL PRIMARY KEY,
            refresh_token VARCHAR(100) UNIQUE NOT NULL,
            token_status VARCHAR(20) DEFAULT "issued",
            FOREIGN KEY(user_id) REFERENCES authentication(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        )
    """
    # UPDATE DATA QUERIES
    UPDATE_VENDOR_ACTIVE_STATUS = """
        UPDATE vendor_table
        SET active_status = "false" 
        WHERE vendor_id = %s 
    """
    UPDATE_DEFAULT_PASSWORD = """
        UPDATE authentication SET password = %s,
        is_changed = "true" WHERE username = %s 
    """
    UPDATE_ASSET_STATUS = """
        UPDATE asset_table 
        SET mapping_id = %s, assigned_to = %s , asset_status = %s, asset_type = %s
        WHERE asset_id = %s     
    """
    UPDATE_ISSUE_STATUS = """
        UPDATE issue_table
        SET issue_status = "resolved", user_id = %s, asset_id = %s 
        WHERE issue_id = %s  
    """
    UPDATE_ASSET_STATUS_UNDER_MAINTENANCE = """
        UPDATE asset_table 
        SET asset_status = "under-maintenance"
        WHERE asset_id = %s     
    """

    UPDATE_ASSET_STATUS_AGAIN_TO_AVAILABLE = """
        UPDATE asset_table 
        SET asset_status = "available"
        WHERE asset_id = %s 
    """
    UPDATE_PASSWORD = """   
        UPDATE authentication
        SET password = %s
        WHERE user_id = %s
    """
    UPDATE_TOKEN_STATUS = """
        UPDATE token_table
        SET token_status = %s
        WHERE access_token = %s
    """
    # FETCH DATA
    FETCH_PASSWORD = """
        SELECT password, role
        FROM authentication
        WHERE user_id = %s
    """
    FETCH_AUTHENTICATION_TABLE = """
        SELECT user_id, username, role
        FROM authentication  
    """
    FETCH_VENDOR_TABLE = """
        SELECT * FROM vendor_table
    """
    FETCH_CATEGORY_TABLE = """
        SELECT * FROM asset_category
    """
    FETCH_CATEGORY_TABLE_WITH_VENDORS = """
        SELECT asset_category.category_id, category_name, brand_name, vendor_table.vendor_name, vendor_table.vendor_email
        FROM asset_category
        INNER JOIN mapping_table ON asset_category.category_id = mapping_table.category_id
        INNER JOIN vendor_table ON mapping_table.vendor_id = vendor_table.vendor_id
    """
    FETCH_ASSETS_TABLE = """
        SELECT asset_table.asset_id, asset_table.asset_type, assigned_to, asset_status,
        asset_category.category_name, vendor_table.vendor_email
        FROM asset_table
        INNER JOIN mapping_table ON asset_table.mapping_id = mapping_table.mapping_id
        INNER JOIN asset_category ON mapping_table.category_id = asset_category.category_id
        INNER JOIN vendor_table ON mapping_table.vendor_id = vendor_table.vendor_id
    """
    FETCH_ASSETS_BY_USER_ID = """
        SELECT authentication.user_id, authentication.username, 
        asset_table.asset_id
        FROM authentication
        INNER JOIN asset_table 
        ON authentication.user_id = asset_table.assigned_to 
        WHERE authentication.user_id = %s  
    """
    FETCH_ASSETS_BY_CATEGORY_ID = """
        SELECT asset_category.category_id, asset_category.category_name, asset_category.brand_name,
        asset_table.asset_id
        FROM asset_category
        INNER JOIN mapping_table ON asset_category.category_id = mapping_table.category_id
        INNER JOIN asset_table ON asset_table.mapping_id = mapping_table.mapping_id
        WHERE asset_category.category_id = %s  
    """
    FETCH_ASSETS_BY_VENDOR_EMAIL = """
        SELECT asset_table.asset_id, asset_table.assigned_to,
        mapping_table.vendor_id, vendor_table.vendor_name, vendor_table.vendor_email
        FROM asset_table
        INNER JOIN mapping_table ON asset_table.mapping_id = mapping_table.mapping_id
        INNER JOIN vendor_table ON mapping_table.vendor_id = vendor_table.vendor_id
        WHERE vendor_table.vendor_email = %s    
    """
    FETCH_ASSETS_AVAILABLE = """
        SELECT * FROM asset_table
        WHERE asset_status = "available"    
    """
    FETCH_ASSETS_UNDER_MAINTENANCE = """
        SELECT * FROM asset_table
        WHERE asset_status = "under_maintenance"
    """
    FETCH_USER_CREDENTIALS = """
        SELECT user_id, password, role, is_changed 
        FROM authentication WHERE username = %s 
    """
    FETCH_ASSIGNED_ASSETS_BY_UID = """
        SELECT asset_table.asset_id, asset_table.assigned_to
        FROM asset_table
        WHERE asset_table.assigned_to = %s
    """
    FETCH_CATEGORY_DETAILS = """
        SELECT asset_category.category_id, asset_category.category_name, asset_category.brand_name, 
        mapping_table.vendor_id, vendor_table.vendor_name, vendor_table.vendor_email, vendor_table.active_status
        FROM asset_category
        INNER JOIN mapping_table ON mapping_table.category_id = asset_category.category_id
        INNER JOIN vendor_table ON mapping_table.vendor_id = vendor_table.vendor_id   
    """
    FETCH_ASSIGNABLE_ASSETS = """
        SELECT asset_table.asset_id, mapping_table.category_id, asset_category.category_name, asset_category.brand_name
        FROM asset_table
        INNER JOIN mapping_table ON asset_table.mapping_id = mapping_table.mapping_id
        INNER JOIN asset_category ON mapping_table.category_id = asset_category.category_id
        WHERE asset_table.asset_type = "assignable" AND asset_table.asset_status = "available"
    """
    FETCH_ASSIGNABLE_ASSETS_TO_ASSIGN = """
        SELECT * FROM asset_table
        WHERE asset_type = "assignable" AND asset_status = "available" 
    """
    FETCH_ASSIGNED_ASSETS_TO_UNASSIGN = """
        SELECT * FROM asset_table
        WHERE asset_type = "assignable" AND asset_status = "unavailable"
    """
    FETCH_FROM_MAPPING_TABLE = """
        SELECT * FROM mapping_table
        WHERE category_id = %s AND vendor_id = %s    
    """
    FETCH_ISSUES_PENDING = """
        SELECT issue_id, user_id, asset_id 
        FROM issue_table
        WHERE issue_status = "pending"  
    """
    FETCH_IF_CATEGORY_EXISTS = """
        SELECT category_name
        FROM asset_category
        WHERE category_id = %s     
    """
    FETCH_IF_ASSET_EXISTS = """
        SELECT mapping_id 
        FROM asset_table 
        WHERE asset_id = %s AND asset_type = "assignable"    
    """
    FETCH_IF_USER_EXISTS = """
    SELECT user_id FROM authentication WHERE user_id = %s
    """
    FETCH_VENDOR_BY_EMAIL = """
        SELECT vendor_id 
        FROM vendor_table 
        WHERE vendor_email = %s AND active_status = "true"    
    """
    FETCH_VENDOR_BY_ID = """
        SELECT vendor_email
        FROM vendor_table 
        WHERE vendor_id = %s AND active_status = "true"    
    """
    FETCH_DETAILS_BY_UID = """
        SELECT user_id, username, role
        FROM authentication
        WHERE user_id = %s
    """
    FETCH_IF_USER_HAVE_ASSET = """
        SELECT mapping_id
        FROM asset_table
        WHERE asset_id = %s AND assigned_to = %s AND asset_status = "unavailable"
    """
    FETCH_MAPPING_ID = """
        SELECT mapping_id 
        FROM mapping_table
        WHERE category_id = %s AND vendor_id = %s
    """
    FETCH_BY_CATEGORY_AND_BRAND_NAME = """
        SELECT category_id
        FROM asset_category
        WHERE category_name = %s AND brand_name = %s
    """
    FETCH_ASSET_ID_BY_ISSUE_ID = """
        SELECT asset_id 
        FROM issue_table
        WHERE issue_id = %s
    """
    FETCH_MAPPINGID = """
        SELECT mapping_id, mapping_table.category_id, asset_category.category_name, asset_category.brand_name,
        mapping_table.vendor_id, vendor_table.vendor_email
        FROM mapping_table 
        INNER JOIN asset_category ON mapping_table.category_id = asset_category.category_id
        INNER JOIN vendor_table ON mapping_table.vendor_id = vendor_table.vendor_id    
    """
    FETCH_IF_MAPPING_ID_EXISTS = """
        SELECT mapping_id 
        FROM mapping_table
        WHERE mapping_id = %s
    """
    INSERT_VENDOR_DETAILS = """
        INSERT INTO vendor_table(
        vendor_id, vendor_name, vendor_email
        ) VALUES (%s, %s, %s)    
    """
    INSERT_CATEGORY_DETAILS = """
        INSERT INTO asset_category(
        category_id, category_name, brand_name
        ) VALUES (%s, %s, %s)   
    """
    INSERY_ASSET_DETAILS = """
        INSERT INTO asset_table(
        asset_id, mapping_id, asset_type
        ) VALUES(%s, %s, %s)
    """
    INSERT_MAPPING_DETAILS = """
        INSERT INTO mapping_table(
        mapping_id,category_id, vendor_id
        ) VALUES (%s, %s, %s)
    """
    INSERT_USER_CREDENTIALS = """
        INSERT INTO authentication
        (user_id, username, password, role)
        VALUES (%s, %s, %s, %s)  
    """
    INSERT_ISSUE_FOR_ASSET = """
        INSERT INTO issue_table(
        issue_id, user_id, asset_id
        ) VALUES (%s, %s, %s)  
    """
    INSERT_TOKEN_DETAILS = """
        INSERT INTO token_table(
        user_id, access_token, refresh_token
        ) VALUES (%s, %s, %s)  
    """
    FETCH_ISSUE_TABLE = """
        SELECT * 
        FROM issue_table
    """
    FETCH_ISSUE_BY_USER_ID = """
        SELECT * 
        FROM issue_table
        WHERE user_id = %s
    """
    FETCH_IF_ISSUE_PENDING = """
        SELECT issue_status
        FROM issue_table
        WHERE issue_id = %s
    """
    FETCH_IF_TOKEN_REVOKED = """
        SELECT token_status
        FROM token_table
        WHERE access_token = %s
    """