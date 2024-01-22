import os
from dotenv import load_dotenv
from src.config.app_config import AppConfig

load_dotenv()

class MappedRole:
    ADMIN_ROLE = os.getenv('ADMIN')
    MANAGER_ROLE = os.getenv('MANAGER')
    EMPLOYEE_ROLE = os.getenv('EMPLOYEE')

    @classmethod
    def get_mapped_role(cls, role: str):
        if role == AppConfig.ADMININSTRATOR:
            return cls.ADMIN_ROLE
        elif role == AppConfig.ASSET_MANAGER:
            return cls.EMPLOYEE_ROLE
        elif role == AppConfig.EMPLOYEE:
            return cls.EMPLOYEE_ROLE
        