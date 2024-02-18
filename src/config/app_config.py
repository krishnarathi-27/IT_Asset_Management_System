"""This module contains all the app constants"""
import os

class AppConfig:
    """Class is used to load all the appconfig constants"""

    PROMPT_FILE_LOCATION = os.path.abspath(os.curdir) + "config/prompts/prompts.yaml"
    MAX_LOGIN_ATTEMPTS = 3
    LOG_LOCATION = r"logs.txt"

    # roles of user
    ADMININSTRATOR = "admin"
    ASSET_MANAGER = "asset manager"
    EMPLOYEE = "employee"

    # regex patterns
    DATE_FORMAT = r"%Y-%m-%d"
    REGEX_USER_ID = r"^EMP[a-zA-Z0-9]{4}$"
    REGEX_ASSET_ID = r"^ASN[a-zA-Z0-9]{4}$"
    REGEX_CATEGORY_ID = r"^CAT[a-zA-Z0-9]{4}$"
    REGEX_MAPPING_ID = r"^MPN[a-zA-Z0-9]{4}$"
    REGEX_VENDOR_ID = r"^VEN[a-zA-Z0-9]{4}$"
    REGEX_ISSUE_ID = r"^ISN[a-zA-Z0-9]{4}$"
    REGEX_MAINTENANCE_ID = r"^MTN[a-zA-Z0-9]{4}$"
    REGEX_NAME = r"^([A-Za-z0-9]{3,20}.\s*)"
    REGEX_EMAIL = r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}"
    REGEX_PASSWORD = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%&]).{8,}$"

    ASSIGNABLE_ASSET_TYPE = "assignable"
    UNASSIGNABLE_ASSET_TYPE = "unassignable"
    UNAVAILABLE_STATUS = "unavailable"
    AVAILABLE_STATUS = "available"
    ASSET_LOCATION = "warehouse"

    SWAGGER_AUTHORISATION_HEADER = [{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}]

class StatusCodes:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    INTERNAL_SERVER_ERROR = 500
