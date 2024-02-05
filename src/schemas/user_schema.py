from marshmallow import Schema, fields,validate
from src.config.app_config import AppConfig

class LoginSchema(Schema):
    username = fields.Str(required=True,validate=validate.Regexp(AppConfig.REGEX_NAME))
    password = fields.Str(required=True)

class LoginSuccessSchema(Schema):
    access_token = fields.Str(dump_only=True)
    # refresh_token = fields.Str(dump_only=True)
    message = fields.Str(dump_only=True)

class UserCreateSchema(Schema):
    user_id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)
    role = fields.Str(required=True)
    message = fields.Str(dump_only=True)

class UserDetailsSchema(Schema):
    user_id = fields.Str(dump_only=True)
    username = fields.Str(dump_only=True)
    role = fields.Str(dump_only=True)

class UserPassword(Schema):
    old_password = fields.Str(required=True)
    new_password = fields.Str(required=True)
    confirm_password = fields.Str(required=True)