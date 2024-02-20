from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig
from src.schemas.config_schema import MySchema

class VendorSchema(MySchema):
    vendor_id = fields.Str(dump_only=True)
    vendor_email = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_EMAIL))
    vendor_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    message = fields.Str(dump_only=True)

class VendorDetailsSchema(MySchema):
    vendor_id = fields.Str(dump_only=True)
    vendor_email = fields.Str(dump_only=True)
    vendor_name = fields.Str(dump_only=True)
    active_status = fields.Str(dump_only=True)

class VendorDeactivateSchema(MySchema):
    message = fields.Str(dump_only=True)

class CategoryDetailsSchema(MySchema):
    category_id = fields.Str(dump_only=True)
    category_name = fields.Str(dump_only=True)
    brand_name = fields.Str(dump_only=True)
    vendor_name = fields.Str(dump_only=True)
    vendor_email = fields.Str(dump_only=True)

class CategorySchema(MySchema):
    category_id = fields.Str(dump_only=True)
    category_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    brand_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    vendor_email = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_EMAIL))
    message = fields.Str(dump_only=True)
    
class ViewAssetSchema(MySchema):     
    asset_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_ASSET_ID))
    category_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    vendor_email = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_EMAIL))
    asset_type = fields.Str(required=True)
    assigned_to = fields.Str(required=True)
    asset_status = fields.Str(required=True)

class AssetSchema(MySchema):
    category_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    brand_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    vendor_email = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_EMAIL))
    asset_type = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    message = fields.Str(dump_only=True)

class AssetUpdateSchema(MySchema):
    mapping_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_MAPPING_ID))
    asset_type = fields.Str(required=True)
    asset_status = fields.Str(required=True)
    assigned_to = fields.Str(required=True)
    message = fields.Str(dump_only=True)
