"""This module contains all the queries of the project"""
from config.prompts.prompts import PromptConfig

PromptConfig.load()


class Header:
    """Header class is used to load headers of tables displayed"""

    SCHEMA_USER_TABLE = (
        PromptConfig.HEADER_USERID,
        PromptConfig.HEADER_USERNAME,
        PromptConfig.HEADER_ROLE,
    )

    SCHEMA_VENDOR_TABLE = (
        PromptConfig.HEADER_VENDOR_ID,
        PromptConfig.HEADER_VENDOR_NAME,
        PromptConfig.HEADER_VENDOR_EMAIL,
        PromptConfig.HEADER_ACTIVE_STATUS,
    )

    SCHEMA_ASSET_TABLE = (
        PromptConfig.HEADER_ASSET_ID,
        PromptConfig.HEADER_ASSET_TYPE,
        PromptConfig.HEADER_ASSIGNED_TO,
        PromptConfig.HEADER_ASSET_STATUS,
        PromptConfig.HEADER_PURCHASED_DATE,
        PromptConfig.HEADER_MAPPING_ID,
    )

    SCHEMA_MAINTENANCE_TABLE = (
        PromptConfig.HEADER_MAINTENANCE_ID,
        PromptConfig.HEADER_ASSET_ID,
        PromptConfig.HEADER_START_DATE,
        PromptConfig.HEADER_RETURN_DATE,
    )

    SCHEMA_CATEGORY_DETAILS_TABLE = (
        PromptConfig.HEADER_CATEGORY_ID,
        PromptConfig.HEADER_CATEGORY_NAME,
        PromptConfig.HEADER_BRAND_NAME,
    )

    SCHEMA_ASSETS_BY_USER_ID = (
        PromptConfig.HEADER_USERID,
        PromptConfig.HEADER_USERNAME,
        PromptConfig.HEADER_ASSET_ID,
        PromptConfig.HEADER_PURCHASED_DATE,
    )

    SCHEMA_ASSETS_BY_CATEGORY_ID = (
        PromptConfig.HEADER_CATEGORY_ID,
        PromptConfig.HEADER_CATEGORY_NAME,
        PromptConfig.HEADER_BRAND_NAME,
        PromptConfig.HEADER_ASSET_ID,
        PromptConfig.HEADER_PURCHASED_DATE,
    )

    SCHEMA_ASSETS_BY_VENDOR_EMAIL = (
        PromptConfig.HEADER_ASSET_ID,
        PromptConfig.HEADER_PURCHASED_DATE,
        PromptConfig.HEADER_ASSIGNED_TO,
        PromptConfig.HEADER_VENDOR_ID,
        PromptConfig.HEADER_VENDOR_NAME,
        PromptConfig.HEADER_VENDOR_EMAIL,
    )

    SCHEMA_ASSETS_TO_USER = (
        PromptConfig.HEADER_ASSET_ID,
        PromptConfig.HEADER_ASSIGNED_TO,
    )

    SCHEMA_PENDING_ISSUES = (
        PromptConfig.HEADER_ISSUE_ID,
        PromptConfig.HEADER_USERID,
        PromptConfig.HEADER_ASSET_ID,
    )

    SCHEMA_ASSIGNABLE_ASSET_DETAILS = (
        PromptConfig.HEADER_ASSET_ID,
        PromptConfig.HEADER_CATEGORY_ID,
        PromptConfig.HEADER_CATEGORY_NAME,
        PromptConfig.HEADER_BRAND_NAME,
    )

    SCHEMA_CATEGORY_TABLE = (
        PromptConfig.HEADER_CATEGORY_ID,
        PromptConfig.HEADER_CATEGORY_NAME,
        PromptConfig.HEADER_BRAND_NAME,
        PromptConfig.HEADER_VENDOR_ID,
        PromptConfig.HEADER_VENDOR_NAME,
        PromptConfig.HEADER_ACTIVE_STATUS,
    )

    SCHEMA_MAPPING_CATGEORY_VENDOR_TABLE = (
        PromptConfig.HEADER_MAPPING_ID,
        PromptConfig.HEADER_CATEGORY_ID,
        PromptConfig.HEADER_CATEGORY_NAME,
        PromptConfig.HEADER_BRAND_NAME,
        PromptConfig.HEADER_VENDOR_ID,
        PromptConfig.HEADER_VENDOR_EMAIL,
    )


class Queries:
    """Queries class is used to load queries"""

    CREATE_AUTHENTICATION_TABLE = """
        CREATE TABLE IF NOT EXISTS authentication(
            user_id TEXT PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT,
            is_changed TEXT DEFAULT "false" 
        )
    """
    CREATE_VENDOR_TABLE = """
        CREATE TABLE IF NOT EXISTS vendor_table(
            vendor_id TEXT PRIMARY KEY,
            vendor_name TEXT,
            vendor_email TEXT UNIQUE,
            active_status TEXT DEFAULT "true"
        )   
    """
    CREATE_ASSET_CATEGORY_TABLE = """
        CREATE TABLE IF NOT EXISTS asset_category(
            category_id TEXT PRIMARY KEY,
            category_name TEXT,
            brand_name TEXT
        )   
    """
    CREATE_MAPPING_TABLE = """
        CREATE TABLE IF NOT EXISTS mapping_table(
            mapping_id TEXT PRIMARY KEY,
            category_id TEXT,
            vendor_id TEXT,
            FOREIGN KEY(category_id) REFERENCES asset_category(category_id),
            FOREIGN KEY(vendor_id) REFERENCES vendor_table(vendor_id)
        )
    """
    CREATE_ASSET_TABLE = """
        CREATE TABLE IF NOT EXISTS asset_table(
            asset_id TEXT PRIMARY KEY,
            mapping_id TEXT,
            asset_type TEXT,
            assigned_to TEXT DEFAULT "location",
            asset_status TEXT DEFAULT "available",
            purchased_date TEXT,
            FOREIGN KEY(mapping_id) REFERENCES asset_category(mapping_id)
        )    
    """
    CREATE_MAINTENANCE_TABLE = """
        CREATE TABLE IF NOT EXISTS maintenance_table(
            maintenance_id TEXT PRIMARY KEY,
            asset_id TEXT,
            start_date TEXT,
            return_date TEXT DEFAULT "pending",
            FOREIGN KEY(asset_id) REFERENCES asset_table(asset_id)
        )    
    """
    CREATE_ISSUE_TABLE = """
        CREATE TABLE IF NOT EXISTS issue_table(
            issue_id TEXT PRIMARY KEY,
            user_id TEXT,
            asset_id TEXT,
            issue_status TEXT DEFAULT "pending",
            issue_resolved_by TEXT DEFAULT "pending",
            FOREIGN KEY(asset_id) REFERENCES asset_table(asset_id),
            FOREIGN KEY(user_id) REFERENCES user_table(user_id)
        )    
    """
    # UPDATE DATA QUERIES
    UPDATE_VENDOR_ACTIVE_STATUS = """
        UPDATE vendor_table
        SET active_status = "false" 
        WHERE vendor_email = ? 
    """
    UPDATE_DEFAULT_PASSWORD = """
        UPDATE authentication SET password = ?,
        is_changed = "true" WHERE username = ?
    """
    UPDATE_ASSET_STATUS = """
        UPDATE asset_table 
        SET assigned_to = ?, asset_status = ? 
        WHERE asset_id = ?    
    """
    UPDATE_ISSUE_STATUS_UNDER_MAINTENANCE = """
        UPDATE issue_table
        SET issue_status = "resolved", issue_resolved_by = ?
        WHERE issue_id = ?    
    """
    UPDATE_ASSET_STATUS_UNDER_MAINTENANCE = """
        UPDATE asset_table 
        SET asset_status = "under_maintenance"
        WHERE asset_id = ?    
    """
    UPDATE_MAINTENANCE_RETURN_DATE = """
        UPDATE maintenance_table
        SET return_date = ?
        WHERE maintenance_id = ?    
    """
    UPDATE_ASSET_STATUS_AGAIN_TO_AVAILABLE = """
        UPDATE asset_table 
        SET asset_status = "available"
        WHERE asset_id = ? 
    """

    # FETCH DATA
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
    FETCH_ASSETS_TABLE = """
        SELECT * FROM asset_table
    """
    FETCH_ASSETS_BY_USER_ID = """
        SELECT authentication.user_id, authentication.username, 
        asset_table.asset_id, asset_table.purchased_date
        FROM authentication
        INNER JOIN asset_table 
        ON authentication.user_id = asset_table.assigned_to 
        WHERE authentication.user_id = ?    
    """
    FETCH_ASSETS_BY_CATEGORY_ID = """
        SELECT asset_category.category_id, asset_category.category_name, asset_category.brand_name,
        asset_table.asset_id, asset_table.purchased_date
        FROM asset_category
        INNER JOIN mapping_table ON asset_category.category_id = mapping_table.category_id
        INNER JOIN asset_table ON asset_table.mapping_id = mapping_table.mapping_id
        WHERE asset_category.category_id = ?    
    """
    FETCH_ASSETS_BY_VENDOR_EMAIL = """
        SELECT asset_table.asset_id, asset_table.purchased_date, asset_table.assigned_to,
        mapping_table.vendor_id, vendor_table.vendor_name, vendor_table.vendor_email
        FROM asset_table
        INNER JOIN mapping_table ON asset_table.mapping_id = mapping_table.mapping_id
        INNER JOIN vendor_table ON mapping_table.vendor_id = vendor_table.vendor_id
        WHERE vendor_table.vendor_email = ?    
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
        FROM authentication WHERE username = ? 
    """
    FETCH_ASSIGNED_ASSETS_BY_UID = """
        SELECT asset_table.asset_id, asset_table.assigned_to
        FROM asset_table
        WHERE asset_table.assigned_to = ?
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
        WHERE category_id = ? AND vendor_id = ?    
    """
    FETCH_ISSUES_PENDING = """
        SELECT issue_id, user_id, asset_id 
        FROM issue_table
        WHERE issue_status = "pending"  
    """
    FETCH_MAINTENANCE_TABLE = """
        SELECT * FROM maintenance_table 
        WHERE return_date = "pending"   
    """
    FETCH_ASSET_ID_BY_MAINTENANCE_TABLE = """
        SELECT asset_id 
        FROM maintenance_table
        WHERE maintenance_id= ?    
    """
    FETCH_IF_CATEGORY_EXISTS = """
        SELECT category_name
        FROM asset_category
        WHERE category_id = ?     
    """
    FETCH_IF_ASSET_EXISTS = """
        SELECT asset_id 
        FROM asset_table 
        WHERE asset_id = ? AND asset_type = "assignable"    
    """
    FETCH_IF_USER_EXISTS = """
    SELECT user_id FROM authentication WHERE user_id = ?
    """
    FETCH_VENDOR_BY_EMAIL = """
        SELECT vendor_id 
        FROM vendor_table 
        WHERE vendor_email = ? AND active_status = "true"    
    """
    FETCH_DETAILS_BY_UID = """
        SELECT user_id, username, role
        FROM authentication
        WHERE user_id = ? 
    """
    FETCH_IF_USER_HAVE_ASSET = """
        SELECT mapping_id
        FROM asset_table
        WHERE asset_id = ? AND assigned_to = ?    
    """
    FETCH_BY_CATEGORY_AND_BRAND_NAME = """
        SELECT category_id
        FROM asset_category
        WHERE category_name = ? AND brand_name = ?    
    """
    FETCH_ASSET_ID_BY_ISSUE_ID = """
        SELECT asset_id 
        FROM issue_table
        WHERE issue_id = ?
    """
    FETCH_MAPPING_ID = """
        SELECT mapping_id, mapping_table.category_id, asset_category.category_name, asset_category.brand_name,
        mapping_table.vendor_id, vendor_table.vendor_email
        FROM mapping_table 
        INNER JOIN asset_category ON mapping_table.category_id = asset_category.category_id
        INNER JOIN vendor_table ON mapping_table.vendor_id = vendor_table.vendor_id    
    """
    FETCH_IF_MAPPING_ID_EXISTS = """
        SELECT mapping_id 
        FROM mapping_table
        WHERE mapping_id = ?
    """
    INSERT_VENDOR_DETAILS = """
        INSERT INTO vendor_table(
        vendor_id, vendor_name, vendor_email
        ) VALUES (?,?,?)    
    """
    INSERT_CATEGORY_DETAILS = """
        INSERT INTO asset_category(
        category_id, category_name, brand_name
        ) VALUES (?,?,?)   
    """
    INSERY_ASSET_DETAILS = """
        INSERT INTO asset_table(
        asset_id, mapping_id, asset_type, purchased_date
        ) VALUES(?,?,?,?)
    """
    INSERT_MAPPING_DETAILS = """
        INSERT INTO mapping_table(
        mapping_id,category_id, vendor_id
        ) VALUES (?,?,?)
    """
    INSERT_IN_MAINTENANCE_TABLE = """
        INSERT INTO maintenance_table (
        maintenance_id, asset_id, start_date
        ) VALUES(?,?,?)  
    """
    INSERT_USER_CREDENTIALS = """
        INSERT INTO authentication
        (user_id, username, password, role)
        VALUES (?,?,?,?)  
    """
    INSERT_ISSUE_FOR_ASSET = """
        INSERT INTO issue_table(
        issue_id, user_id, asset_id
        ) VALUES (?,?,?)  
    """
