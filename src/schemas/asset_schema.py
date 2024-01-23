from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig

class VendorSchema(Schema):
    vendor_id = fields.Str(dump_only=True)
    vendor_email = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_EMAIL))
    vendor_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    message = fields.Str(dump_only=True)

class VendorDetailsSchema(Schema):
    vendor_id = fields.Str(dump_only=True)
    vendor_email = fields.Str(dump_only=True)
    vendor_name = fields.Str(dump_only=True)
    active_status = fields.Str(dump_only=True)

class VendorDeactivateSchema(Schema):
    message = fields.Str(dump_only=True)

class CategoryDetailsSchema(Schema):
    category_id = fields.Str(dump_only=True)
    category_name = fields.Str(dump_only=True)
    brand_name = fields.Str(dump_only=True)
    vendor_name = fields.Str(dump_only=True)
    vendor_email = fields.Str(dump_only=True)

class CategorySchema(Schema):
    category_id = fields.Str(dump_only=True)
    category_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    brand_name = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    vendor_email = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_EMAIL))
    message = fields.Str(dump_only=True)
    