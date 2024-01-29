from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig

class IssueSchema(Schema):
    issue_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_ISSUE_ID))
    asset_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_ASSET_ID))
    user_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_USER_ID))
    issue_status = fields.Str(required=True)

class IssueCreateSchema(Schema):
    asset_id = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_ASSET_ID))
    