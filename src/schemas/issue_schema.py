from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig
from src.schemas.config_schema import MySchema

class IssueSchema(MySchema):
    issue_id = fields.Str(dump_only=True,validate=validate.Regexp(AppConfig.REGEX_ISSUE_ID))
    asset_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_ASSET_ID))
    user_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_USER_ID))
    issue_status = fields.Str(required=True)

class IssueCreateSchema(MYSchema):
    asset_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_ASSET_ID))
    